import binascii
import socket
import struct
import sys
import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('gains.conf')
kP = config.get('gains', 'kP')
kI = config.get('gains', 'kI')
kD = config.get('gains', 'kD')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_IP = '119.9.21.113'
TCP_PORT = 5005
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

unpacker = struct.Struct('15f')
packer = struct.Struct('1f')

while True:
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)

        errorList = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', errorList

        print errorList[3]

        #PID Control
        effort = kP*errorList[1] + kI*(sum(errorList[0:5])) + kD*(errorList[1]-errorList[2])
        packed_data = packer.pack(*effort)
        connection.send(packed_data)
        
    finally:
        connection.close()
        print 'close'
