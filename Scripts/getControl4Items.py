"""
Author: sapatel91
Date: March 2, 2014
File: getControl4Items.py

Purpose: Prints ID and Name of various items from a Control4 system

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
"""

from bs4 import BeautifulSoup
from PyControl4 import connection

# Insert the IP of your Control4 system here. Can be obtained from Composer.
TCP_IP = "192.168.1.25"  # Will need to change for your system's IP
TCP_PORT = 5021
BUFFER_SIZE = 8192

# Function used to extract text between tags
# For example "<value> 43 </value>" returns 43
def getText(soupData, tag):
    tag = soupData.find(tag)
    try:
        text_parts = tag.findAll(text=True)
        text = "".join(text_parts)
        return text.strip()
    except:
        return "Value not found!"


# Connect to Director and issue soap command to get all items on system.
connection.C4SoapConn(TCP_IP, TCP_PORT)
MESSAGE = '<c4soap name="GetItems" async="False"><param name="filter" type="number">0</param></c4soap>'
data_soup = connection.C4SoapConn.Send(MESSAGE)
data = str(data_soup)
out_string = ""
while not "</c4soap>" in data:
    out_string += data
    if "</c4soap>" in data:
        break
soapData = BeautifulSoup(out_string, "lxml-xml")
# directorConn.close()

# Parse SOAP data
items = soapData.findAll("item")
for item in items:
    """
        Change the type value for the following:
            2 - Site
            3 - Building
            4 - Floor
            6 - Device Type
            7 - Device
            8 - Room
    """
    if getText(item, "type") == "7":
        print("{1}, {2}".format(getText(item, "id"), getText(item, "name")))

