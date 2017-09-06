# import time
# import serial

# # configure the serial connections (the parameters differs on the device you are connecting to)
# ser = serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1
# )

# ser.isOpen()
# out = ''
# print 'This program will continually loop looking for recieved messages'
# while 1:
#         while ser.inWaiting() > 0:
#             out += ser.read(1)

#         if out != '':
#             print ">>" + out

import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=1000000)
    data = []
    time0 = time.time()
    while (time.time() - time0 < 5):  # Read data for 5 seconds
        data.append(ser.readline())
    ser.close()
    print ">>" + data