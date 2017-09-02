import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.isOpen()
out = ''
print 'This program will continually loop looking for recieved messages'
while 1:
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out