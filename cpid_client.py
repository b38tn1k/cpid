import binascii
import socket
import struct
import sys
import time

err = 1
lpTm = 0

# Create a TCP/IP socket
TCP_IP = 'cpid.io'
TCP_PORT = 5005
while True:

    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #pack error, time code, sequence number into a struct to simplify send
    values = (err, errSum, errLast, lpTm, seqNum)
    packer = struct.Struct('5f')
    packed_data = packer.pack(*values)
    unpacker = struct.Struct('1f')
    
    
    try:
        # Send data
        print >>sys.stderr, 'sending...'
        sock.send(packed_data)
        data = sock.recv(unpacker.size);
        effort = unpacker.unpack(data)
        print 'effort: "%s"' % effort
        
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
        seqNum += 1
        errLast = err
        lpTm = time.time() - start_time
        errSum += (err*lpTm)
        print lpTm, "seconds"


