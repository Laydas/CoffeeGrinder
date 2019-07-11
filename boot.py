# Import socket for API usage
try:
    import usocket as socket
except:
    import socket

# Import libraries for gpio usage
from machine import Pin
import network

import gc
# import webrepl
# webrepl.start()
gc.collect()

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection Successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)

import readPot
