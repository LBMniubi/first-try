
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['axes.unicode_minus']=False
C=1;a=-0.6;b=0.6;c=0
t=np.arange(-2,2,0.01)
x1=C*np.exp(a*t)
x2=C*np.exp(b*t)
x3=C*np.exp(c*t)


plt.subplot(2,2,2)
A=1;w=0.5*np.pi;fi=np.pi/6
t1=np.arange(0,8,0.001)
x4=np.cos(w*t1+fi)
plt.plot(t1,x4)
plt.axis([0,8,-1,1])
plt.title('正弦信号')
plt.xlabel('t1')
plt.ylabel('x4(t)')

plt.subplot(2,2,3)
t2=np.arange(0,8,0.001)
w1=2*np.pi
x5=C*np.exp(a*t2)*np.cos(w1*t1+fi)
plt.plot(t2,x5)
plt.axis([0,8,-1,1])
plt.title('幅度衰减正弦信号')
plt.xlabel('t2')
plt.ylabel('x5(t)')

plt.subplot(2,2,4)
t2=np.arange(0,8,0.001)
w1=2*np.pi
x6=C*np.exp(b*t2)*0.01*np.cos(w1*t1+fi)
plt.plot(t2,x6)
plt.axis([0,8,-1,1])
plt.title('幅度增长正弦信号')
plt.xlabel('t2')
plt.ylabel('x5(t)')

plt.show()