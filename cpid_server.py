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

unpacker = struct.Struct('5f')
packer = struct.Struct('1f')

while True:
    start_time = time.time()
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        #print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)
        print 'recieving'

        errList = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', errList

        #PID Control
        effort = kP*errList[1] + kI*(errList[2]+errList[1]) + kD*(errList[1]-errList[3])
        print 'effort: "%s"' % effort

        packed_data = packer.pack(effort)
        connection.send(packed_data)
    except:
        pass
    finally:
        connection.close()
        print 'close'
        print time.time() - start_time, "seconds"
