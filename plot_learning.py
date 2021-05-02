import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


t = np.arange(0,360,1)
y = np.sin(t*np.pi/180)
z = np.arange(0,360,1)

x1 = np.array([0,10,20])
y1 = np.array([0,10,20])
z1 = np.array([0,10,20])

xlink1 = np.array([0,5])
ylink1 = np.array([0,5])
zlink1 = np.array([0,5])

xlink2 = np.array([5,10])
ylink2 = np.array([5,10])
zlink2 = np.array([5,10])




# plt.plot(t,y,'r')
# plt.axes(0,360,-1,1)
 # plt.grid(True)
world = plt.axes(projection='3d')

plt.plot(xlink1,ylink1,zlink1,'r')
plt.plot(xlink2,ylink2,zlink2,'b')


# plt.plot(x1,y1,z1,'r')
# plt.plot(t,y,z,'r')
plt.xlabel('x axis')
plt.ylabel('y axis')
# plt.zlabel('z axis')

plt.show()





























