###############################
############CPID###############
###############################
import binascii
import socket
import struct
import sys
import time
import serial
# Create a TCP/IP socket
TCP_IP = 'cpid.io'
TCP_PORT = 5005
#Create output files
outTXT = open('OutPut.txt', 'w')
outTXT.write('Output: ')
timeTXT = open('Time.txt', 'w')
timeTXT.write('Time: ')
#serial connection with Arduino
ser = serial.Serial('/dev/tty.usbmodem641', 115200)
#initialise values
SetPoint = 100
lpTm = 1
VelScale = 12 #value to scale encoder with H-Bridge/DC Motor
errSum = errLast = seqNum = err = effort = Pos = OldPos = Vel = OldVel = clTm = 0
print('Setup Complete')

while True:
    start_time = time.time()
    
    #hacky error catching and negative number byte send
    negflag = 1
    if (effort<0):
        negflag = 2
    if(abs(effort)>255):
        effort = 255
        
    #write effort to Arduino
    ser.write(bytes(chr(negflag)))
    ser.write(bytes(chr(abs(effort))))
    
    #read in position from Arduino
    if ser.inWaiting()>2:
        print('Reading New Position')
        neg = ser.read()
        Pos = ser.read()
        Pos = ord(Pos)+ord(ser.read())*256
        if (ord(neg) == 1):
            Pos = -Pos
        ser.flushInput()
        print 'Position: ' + str(Pos)
        Vel = (OldPos - Pos)/(VelScale*lpTm)
        if (Vel > (OldVel + 255) or Vel < (OldVel - 255)):
            Vel = OldVel
            print 'Position Read Error!'
        OldVel = Vel
        print 'Velocity: ' + str(Vel)
        OldPos = Pos
        
    err = SetPoint - Vel
    #err = SetPoint - Pos
    #empty value jitter
    if(err == 0):
        err = err+0.01
        
    print 'Setpoint: ' + str(SetPoint)
    print 'Error: ' + str(err)
    #read in position from Arduino here
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #pack error, time code, sequence number into a struct to simplify send
    values = (err, errSum, errLast, lpTm, seqNum)
    packer = struct.Struct('5f')
    packed_data = packer.pack(*values)
    unpacker = struct.Struct('1f')


    try:
        #send data
        print >>sys.stderr, 'sending...'
        sock.send(packed_data)
        #recieve data
        data = sock.recv(unpacker.size);
        effort = unpacker.unpack(data)
        effort = int(effort[0])
        print 'Control Effort: ' + str(effort)
        
    except:
        print >>sys.stderr, 'closing socket'
        sock.close()
    seqNum += 1
    print 'Sequence Number: ' + str(seqNum)
    errLast = err
    lpTm = time.time() - start_time
    errSum += (err*lpTm)
    print 'Loop Time: ' + str(lpTm), "seconds"
    clTm += lpTm
    #record output
    outTXT.write(str(Vel) + ', ')
    outTXT.flush()
    timeTXT.write(str(clTm) + ', ')
    timeTXT.flush()
    if(seqNum > 100):
        #Beep! experiment over
        sys.stdout.write('\a')
        time.sleep(1)
        sys.stdout.flush()
        #close text files
        outTXT.close()
        timeTXT.close()
        sys.exit
