'''
Author: lawtancool, sapatel91
Date: June 8, 2020
File: TestSendSOAP.py

Purpose: Send SOAP Commands to C4

Disclaimer: USE AT YOUR RISK, I TAKE NO RESPONSIBILITY
            Most likely there won't be any though
'''

# from PyControl4.connection import C4SoapConn
# from PyControl4.light import C4Light

from PyControl4 import connection
from PyControl4 import light

# Establish Connection
# NOTE: IP Address will be different for your system
connection.C4SoapConn('192.168.1.25', 5021)

light = light.C4Light(253)
print(light.getLevel())
# light.rampToLevel(100, 10000)
# Pulse Volume Down in Family Room
#Message = '<c4soap name="SendToDeviceAsync" async="1" seq="1615"><param name="iddevice" type="number">10</param><param name="data" type="string"><devicecommand><command>PULSE_VOL_DOWN</command><params></params></devicecommand></param></c4soap>'
#C4SoapConn.Send(Message)