"""
Author: lawtancool, sapatel91
Date: June 8, 2020
File: media.py

Purpose: Control Control4 media (requires C4SoapConn to be setup by the caller script)

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
"""

from .connection import C4SoapConn
from bs4 import BeautifulSoup


class C4Remote:
    def VolDown(self):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="iddevice" type="number">10</param><param name="data" type="string"><devicecommand><command>PULSE_VOL_DOWN</command><params></params></devicecommand></param></c4soap>'
        C4SoapConn.Send(MESSAGE)

    def VolUp(self):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="iddevice" type="number">10</param><param name="data" type="string"><devicecommand><command>PULSE_VOL_UP</command><params></params></devicecommand></param></c4soap>'
        C4SoapConn.Send(MESSAGE)

    def Info(self):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="iddevice" type="number">10</param><param name="data" type="string"><devicecommand><command>INFO</command><params></params></devicecommand></param></c4soap>'
        C4SoapConn.Send(MESSAGE)

    def Cancel(self):
        MESSAGE = '<c4soap name="SendToDeviceAsync" async="1"><param name="iddevice" type="number">10</param><param name="data" type="string"><devicecommand><command>CANCEL</command><params></params></devicecommand></param></c4soap>'
        C4SoapConn.Send(MESSAGE)
