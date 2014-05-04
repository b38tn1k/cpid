#!/usr/bin/env python

import socket
import web

#Front Page (port 8080)
urls = (
  '/', 'Index'
)

front_page = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "A Cloud Based PID Controller intended to demonstrate the possibilities of applying web-based services to robotics. \nA PID controller is to be designed to operate on a host server and provide control data to a client via the Internet. \nAs the controller will have to operate in real time, packet loss and network latency will have to be accounted for. \nA client account will allow developers to choose gain values for the PID controller. \nThe server and the client will have different data communication responsibilities during operation.\nError is calculated on the client side of the Internet to minimise latency and allow the client to dynamically change set point. \nA server based PID controller will be complemented with a simple linear predictor that utilises the current latency value \nin an attempt to time the arrival of a control effort data packet at the client in such a way that minimises error. \nBoth the Control Effort and Error data will be sent accompanied by a time code and sequence number to allow for packet confirmation. \n"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    front_page.run()
#Server (port 5005)
TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()
