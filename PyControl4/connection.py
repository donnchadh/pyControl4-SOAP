"""
Author: lawtancool, sapatel91
Date: June 8, 2020
File: connection.py

Purpose: Creates connection to Control4 Director

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
"""

import ssl
import socket
from bs4 import BeautifulSoup

# Global variable used to share socket connection between classes
socketConn = 0
BUFFER_SIZE = 8192


class C4SoapConn:
    """
    Establish connection to Control4 system
    Parameters: 
        TCP_IP - IP Address of system
        TCP_PORT - should be 5021 (5020 for non-SSL, depreciated)
    """

    def __init__(self, TCP_IP, TCP_PORT):
        socketNonSSL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global socketConn
        socketConn = ssl.wrap_socket(socketNonSSL)
        socketConn.connect((TCP_IP, TCP_PORT))

    # @staticmethod
    def Send(MESSAGE):
        socketConn.sendall((MESSAGE + "\0").encode())
        data = socketConn.recv(BUFFER_SIZE)
        data = BeautifulSoup(data, "lxml-xml")
        return data

    def GetItems(self):
        MESSAGE = '<c4soap name="GetItems" async="False"> <param name="filter" type="number">0</param></c4soap>'
        socketConn.sendall((MESSAGE + "\0").encode())
        data = socketConn.recv(BUFFER_SIZE)
        data = BeautifulSoup(data, "lxml-xml")
        return data

    def GetNetworkBindings(self):
        MESSAGE = '<c4soap name="GetNetworkBindings" async="False"> <param name="filter" type="number">0</param></c4soap>'
        socketConn.sendall((MESSAGE + "\0").encode())
        data = socketConn.recv(BUFFER_SIZE)
        data = BeautifulSoup(data, "lxml-xml")
        return data
