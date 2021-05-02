import numpy as np
import math
import matplotlib.pyplot as plt


t = np.arange(0,2,0.1)
x = (6.1538 * math.e**(-3*t) ) - (0.1538 * math.cos(2*t)) +(0.237*math.sin(2*t))


plt.plot(t,x,'b')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

