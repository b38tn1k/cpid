#CPID - Cloud Based PID controller (Server)
#James Carthew 2014
#jamesrobertcarthew@gmail.com

import ConfigParser

#read PID gains from gains.conf
config = ConfigParse.RawCOnfigParser()
config.read('gains.conf')
kP = config.get('gains', 'kP')
kI = config.get('gains', 'kI')
kD = config.get('gains', 'kD')

#read from client to array
error = [1, 2, 3, 4, 5]
timeStamp = [0.1, 0.2, 0.3, 0.4, 0.5]
seqNum = [1, 2, 3, 4, 5]

#Proportional Controller Effort and Linear Prediction Filter

#Integral Controller Effort and Linear Prediction Filter

#Derivative Controller Effort and Linear Prediction Filter

#Push To Client



