#!/usr/bin/env python

import time
import serial

ser = serial.Serial(

    port='/dev/ttyUSB2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def sendATcmd(atcmd):
    out = ''
    ser.write(atcmd + '\r\n')
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out != '':
        print ">>" + out


sendATcmd('ATI')
sendATcmd('AT+CIMI')
sendATcmd('AT+CSQ')
sendATcmd('AT+CREG?')
sendATcmd('AT+COPS?')