#display randon motion in 2 d plane
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

N,d= 3,2
x0=np.random.rand(d,N)
steps=300
T=300.
dt=T/steps
time =0.0
xstore=np.zeros([d,N,steps+1])
xstore[:,:,0]=x0
x=x0
counter=1
graph1=plt.plot(xstore[0,0,:],xstore[1,0,:],'r',linewidth=2.) [0]
graph2=plt.plot(xstore[0,1,:],xstore[1,1,:],'g',linewidth=2.) [0]
graph3=plt.plot(xstore[0,2,:],xstore[1,2,:],'b',linewidth=2.) [0]
while time<T:
    
   x=x+np.reshape(norm.rvs(size=d*N),(d,N))*np.sqrt(dt)
   xstore[:,:,counter]=x
   graph1.set_xdata(xstore[0,0,:counter])
   graph1.set_ydata(xstore[1,0,:counter])
   graph2.set_xdata(xstore[0,1,:counter])
   graph2.set_ydata(xstore[1,1,:counter])
   graph3.set_xdata(xstore[0,2,:counter])
   graph3.set_ydata(xstore[1,2,:counter])
   
   plt.xlim([-40.,40.])
   plt.ylim([-40.,40.])
   plt.draw()
   plt.pause(0.02)
   counter+=1
   time+=dt

 

