import time
import serial
import json
import urllib.request

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    #port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.isOpen()
out = ''
print ('This program will continually loop looking for recieved messages')
data = ''
while ser.inWaiting() == 0:
    if ser.inWaiting() > 0:
        # data += ser.readline()
        # print (">>" + data)
        # data = ''
        url = "https://google.com"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        print(response.read())
