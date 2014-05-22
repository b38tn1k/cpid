import binascii
import socket
import struct
import sys
import ConfigParser
import time


config = ConfigParser.RawConfigParser()
config.read('gains.conf')
kP = float(config.get('gains', 'kP'))
kI = float(config.get('gains', 'kI'))
kD = float(config.get('gains', 'kD'))

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_IP = '119.9.21.113'
TCP_PORT = 5005
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

unpacker = struct.Struct('15f')
packer = struct.Struct('1f')

while True:
    start_time = time.time()
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        #print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)
        print 'recieving'

        errorList = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', errorList

        #PID Control
        Integral=float(sum(errorList[0:5]))
        Diff=float(errorList[1]-errorList[2])
        effort = kP*float(errorList[1]) + kI*Integral + kD*Diff
        print 'effort: "%s"' % effort

        packed_data = packer.pack(effort)
        connection.send(packed_data)
        
    finally:
        connection.close()
        print 'close'
        print time.time() - start_time, "seconds"
