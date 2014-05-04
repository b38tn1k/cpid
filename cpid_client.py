import binascii
import socket
import struct
import sys

while True: # Loop until key interupt

    # Create a TCP/IP socket for sending
    TCP_IP = '119.9.21.113'
    TCP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    
    # Pack error, time code, sequence number into a struct to simplify send
    values = (1, 25, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5)
    packer = struct.Struct('15f')
    packed_data = packer.pack(*values)

    try:
        
        # Send data
        print >>sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
        sock.sendall(packed_data)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

