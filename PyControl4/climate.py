"""
Author: lawtancool, sapatel91
Date: June 8, 2020
File: light.py

Purpose: Control Control4 lights (requires C4SoapConn to be setup by the caller script)

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
"""

from .connection import C4SoapConn
from bs4 import BeautifulSoup


class C4Climate:
    """
    Instantiate light object with id
    Parameters: 
        id - device id
    """

    def __init__(self, id):
        self.id = id

    """
    Sets target heating temperature
    Parameters: 
        value - temperature in degrees Celsius
    """

    def setHeatTemp(self, value):
        MESSAGE = (
            '<c4soap name="SendToDeviceAsync" async="1"><param name="data" type="STRING"><devicecommand><command>SET_SETPOINT_HEAT</command><params><param><name>CELSIUS</name><value type="INT"><static>%d</static></value></param></params></devicecommand></param><param name="idDevice" type="INT">%d</param></c4soap>'
            % (value, self.id)
        )
        C4SoapConn.Send(MESSAGE)

    """
    Returns the light level for a dimmer. Value between 0 and 100.
    NOTE: will return an error if used on light switches use getLightState instead
    """

    def getLevel(self):
        MESSAGE = (
            '<c4soap name="GetVariable" async="False"><param name = "iddevice" type = "INT">%d</param><param name = "idvariable" type = "INT">1001</param></c4soap>'
            % (self.id)
        )
        data = C4SoapConn.Send(MESSAGE)
        value = data.find("variable")
        value = value.findAll(text=True)
        value = "".join(value)
        return int(value)

    """
    Returns the light state. Output is 0 or 1.
    """

    def getLightState(self):
        MESSAGE = (
            '<c4soap name="GetVariable" async="False"><param name = "iddevice" type = "INT">%d</param><param name = "idvariable" type = "INT">1000</param></c4soap>'
            % (self.id)
        )
        data = C4SoapConn.Send(MESSAGE)
        value = data.find("variable")
        value = value.findAll(text=True)
        value = "".join(value)
        return int(value)
