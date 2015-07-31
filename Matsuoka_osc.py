## Matsuoka Oscillator 

## Some parameters makes this oscillator stable
## This can be useful for some joints
## Relationship between parameters for oscillation
## 1+tau/T<a<1+b
## 'Analysis of neural oscillator', Matsuoka
## We can restrict the output inside certain values
## by using g function and c parameter

import numpy as np
import matplotlib.pyplot as plt

numOsc=4 # Number of Oscillator

h=1e-3
tau=0.001
T=0.01
a=10.5
b=20.5
c=3.7
#A=(1-np.eye(numOsc))#*np.random.rand(numOsc,numOsc)
A=.5*np.array([[0,-1,-1,1],[-1,0,1,-1],[-1,1,0,-1],[1,-1,-1,0]])
#A=np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])



# Initials of oscillators
x=np.zeros((numOsc,1))+np.array([[0.1],[0.1],[0.2],[0.2]])#np.random.rand(numOsc,1)
v=np.zeros((numOsc,1))+np.array([[0.1],[0.1],[0.2],[0.2]])#np.random.rand(numOsc,1)
y=np.zeros((numOsc,1))+np.array([[0.1],[0.1],[0.2],[0.2]])#np.random.rand(numOsc,1)

#x=[np.random.rand(),np.random.rand()]
#v=[np.random.rand(),np.random.rand()]
#y=[np.random.rand(),np.random.rand()]



g=lambda x:max(0.,x)

yRec0=[]
yRec1=[]
yRec2=[]
yRec3=[]
stopTime=20000
for t in range(stopTime):
    x=x+h*(-x+c-A.dot(y)-b*v)/tau
    v=v+h*(-v+y)/T
    for i in range(numOsc):
        y[i]=g(x[i])
    #print(x,v,y,t,'\n\n')
##    x[0]=x[0]+h*(-x[0]+c-a*y[1]-b*v[0])/tau
##    v[0]=v[0]+h*(-v[0]+y[0])/T
##    y[0]=g(x[0])
##
##    x[1]=x[1]+h*(-x[1]+c-a*y[0]-b*v[1])/tau
##    v[1]=v[1]+h*(-v[1]+y[1])/T
##    y[1]=g(x[1])

    yRec0.append(float(y[0]))
    yRec1.append(float(y[1]))
    yRec2.append(float(y[2]))
    yRec3.append(float(y[3]))
    xx=x[0]-x[1]
    vv=v[0]-v[1]
    XX=x[0]+x[1]
    VV=v[0]+v[1]

time=np.arange(0,stopTime*h,h)
plt.plot(time,yRec0,'ro',linewidth=1.,label='1st output')
plt.plot(time,yRec1,'--',linewidth=3.,label='2nd output')
plt.plot(time,yRec2,'c*',label='3rd output')
plt.plot(time,yRec3,'g',label='4th output')
plt.title('Outputs of {0:d} neurons of Matsuoka Oscillator\n'.format(numOsc)+\
          'tau={0:.2f}, T={1:.2f}, a={2:.2f}, b={3:.2f}, c={4:.2f}'\
          .format(tau,T,a,b,c))
plt.xlabel('Time [sec]')
plt.ylabel('Value of outputs')
plt.legend()
plt.show()
