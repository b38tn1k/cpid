import binascii
import socket
import struct
import sys
import time
import serial

SetPoint = 500


lpTm = errSum = errLast = seqNum = err = val = effort = 0
Pos = 0
i=1
#serial connection with Arduino
ser = serial.Serial('/dev/tty.usbmodem641', 9600)

###############################
############CPID###############
###############################
print('Setup Complete')


while True:
    start_time = time.time()
    time.sleep(0.01)
    if(ser.inWaiting()>0):
        Pos = ser.readline()
        print Pos
    ser.write(i)
    i+=1





