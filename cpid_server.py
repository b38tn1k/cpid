import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_IP = '119.9.21.113'
TCP_PORT = 5005
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

unpacker = struct.Struct('15f')

while True:
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)

        unpacked_data = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', unpacked_data
        
    finally:
        connection.close()
