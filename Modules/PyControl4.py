'''
Author: sapatel91
Date: March 29, 2014
File: Control4Lights.py

Purpose: Encapsulate Control4 Devices

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
'''

import socket

#Global variable used to share socket connection between classes
socketConn = 0

class C4SoapConn:
    def __init__(self, TCP_IP, TCP_PORT):
        global socketConn
        socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketConn.connect((TCP_IP, TCP_PORT))

class C4Light:
    '''
    Instantiate light object with id
    Parameters: 
        id - device id
    '''
    def __init__(self, id):
        self.id = id
    
    '''
    Sets intensity of dimmer switch
    Parameters: 
        value - 0 to 100
    '''
    def setLevel(self,value):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>SET_LEVEL</command><params><param><name>LEVEL</name><value type="INT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>' % (value, self.id)
        socketConn.sendall(MESSAGE + "\0")
    
    '''
    Ramps to a specified level in milliseconds
    Parameters:
        percent - Intensity
        time - Duration in milliseconds
    '''
    def rampToLevel(percent, time):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>RAMP_TO_LEVEL</command><params><param><name>TIME</name><value type="INTEGER"><static>%d</static></value></param><param><name>LEVEL</name><value type="PERCENT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>' % (time, percent, self.id)
        socketConn.sendall(MESSAGE + "\0")

        
        
        
    