import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import math
import random
 
row = 4
col = 4
 
N = 500
fs = 5
n = [2*math.pi*fs*t/N for t in range(N)]    

axis_x = np.linspace(0,3,num=N)
 

x = [math.sin(i) for i in n]
pl.subplot(221)
pl.plot(axis_x,x)
pl.title(u'5Hz的正弦信号')
pl.axis('tight')
 

 
pl.show()
