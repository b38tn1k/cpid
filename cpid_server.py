#CPID - Cloud Based PID controller
#James Carthew 2014
#jamesrobertcarthew@gmail.com
import ConfigParser

def cpid(error, timeStamp, seqNum):

#read PID gains from gains.conf
    config = ConfigParser.RawConfigParser()
    config.read('gains.conf')
    kP = config.get('gains', 'kP')
    kI = config.get('gains', 'kI')
    kD = config.get('gains', 'kD')
#print Incomming Values
    print ("Incomming Error:  "+str(error).strip('[]'))
    print ("Time Stamp:       "+str(timeStamp).strip('[]'))
    print ("Sequence Number:  "+str(seqNum).strip('[]'))    
#PID Controller
#u(t) = kP*e(t) + kI*integral(e(tau)) + kD*(d/dt)e(t)
    
#Proportional Controller Effort and LPF: kP*e(t)
    pCE = kP*error[0]
#Integral Controller Effort and LPF: kI*integral(e(tau))
    iCE = kI*sum(error)
#Derivative Controller Effort and LPF: kD*(d/dt)e(t)
    dCE = kD*(error[0]-error[1])
    print pCE
    print iCE
    print dCE
#Return
    return (pCE+iCE+dCE)

effort = cpid([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])
print ("Control Effort:   " + effort)
