import binascii
import socket
import struct
import sys

while True
    # Create a TCP/IP socket for recieving
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_IP = '119.9.21.113'
    TCP_PORT = 5005
    # Create a struct to unpack data
    unpacker = struct.Struct('15f'):
    # Listen for client
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)
        
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)

        unpacked_data = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', unpacked_data
        
    finally:
        connection.close()
    
        
     # Create a TCP/IP socket for sending
    TCP_IP = client_address
    TCP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
       
    # Pack error, time code, sequence number into a struct to simplify send
    packer = struct.Struct('15f')
    packed_data = packer.pack(*unpacked_data)

    print("Echo")

    try:
            
        # Send data
        print >>sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
        sock.sendall(packed_data)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
