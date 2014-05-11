import binascii
import socket
import struct
import sys
import time

# Create a TCP/IP socket
TCP_IP = 'cpid.io'
TCP_PORT = 5005
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #pack error, time code, sequence number into a struct to simplify send
    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5)
    packer = struct.Struct('15f')
    packed_data = packer.pack(*values)
    
    try:
        # Send data
        print >>sys.stderr, 'sending...'
        sock.send(packed_data)
        effort = sock.recv(3);
        print effort
        
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()


