#CPID - Cloud Based PID controller (Server)
#James Carthew 2014
#jamesrobertcarthew@gmail.com

import ConfigParser

#read PID gains from gains.conf
config = ConfigParser.RawConfigParser()
config.read('gains.conf')
kP = config.get('gains', 'kP')
kI = config.get('gains', 'kI')
kD = config.get('gains', 'kD')  nano

#read from gains to array
error = [1, 2, 3, 4, 5]
timeStamp = [0.1, 0.2, 0.3, 0.4, 0.5]
seqNum = [1, 2, 3, 4, 5]

#PID Controller
#u(t) = kP*e(t) + kI*integral(e(tau)) + kD*(d/dt)e(t)

#Proportional Controller Effort and LPF: kP*e(t)
pCE = kP*error[0]
#Integral Controller Effort and LPF: kI*integral(e(tau))
iCE = kI*
#Derivative Controller Effort and LPF: kD*(d/dt)e(t)

#Push to Client
