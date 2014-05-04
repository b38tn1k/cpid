#!/usr/bin/env python

import socket
import web

#Server (port 5005)
TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

unpacker = struct.Struct('f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, ')
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    unpacked_data = unpacker.unpack(data)
    print "received data:", unpacked_data
    conn.send(unpacked_data)  # echo
conn.close()
