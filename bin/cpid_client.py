import socket

#TCP/IP Server Address, Port Number and Buffer Size
TCP_IP = '119.9.21.113'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#Make Connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

values = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
packer = struct.Struct('f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, ')
packed_data = packer.pack(*values)

s.sendall(packed_data)
data = s.recv(BUFFER_SIZE)

#break
s.close()

print "received data:", data
