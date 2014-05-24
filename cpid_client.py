import binascii
import socket
import struct
import sys
import time

lpTm = errSum = errLast = seqNum = 0

def getErr():
    #use this function to call error values on client side
    err = 10
    return err

def sendCTL(effort):
    #use this function to send control from client to peripheral
    print effort
    return


# Create a TCP/IP socket
TCP_IP = 'cpid.io'
TCP_PORT = 5005

while True:
    start_time = time.time()
    err = getErr()
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
        sendCTL(effort)
        
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
        seqNum += 1
        errLast = err
        lpTm = time.time() - start_time
        errSum += (err*lpTm)
        print lpTm, "seconds"



