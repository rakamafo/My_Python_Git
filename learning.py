import numpy as np
import matplotlib.pyplot as plt
import random
import time
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import style
import math




# for 3D ploting
style.use('fivethirtyeight')
fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)        # for 2d Plotting
ax1 = p3.Axes3D(fig)       # for 3D plotting
ax1.clear()  # clears the plot every iteration
# Setting the axes properties
ax1.set_xlim3d([-10.0, 10.0])
ax1.set_xlabel('X')
ax1.set_ylim3d([-10.0, 10.0])
ax1.set_ylabel('Y')
ax1.set_zlim3d([-10.0, 10.0])
ax1.set_zlabel('Z')
ax1.set_title('3D Test')
# PLot Origin and Axis.
l = 10  # length of the axis.
ax1.plot([0, l], [0, 0], [0, 0], 'r', lw=1)  # X axis
ax1.plot([0, 0], [0, l], [0, 0], 'g', lw=1)  # Y axis
ax1.plot([0, 0], [0, 0], [0, l], 'b', lw=1)  # Z axis


g = 5
n = g*2 +1
x = np.linspace(-g,g,n)
y = np.linspace(-g,g,n)
# z = np.linspace(-g,g,n)

i = np.ones((11,11))
X = i * x
X = X.reshape(1,n*n)

Y = np.rot90(i * y)
Y = Y.reshape(1,n*n)

# Z = np.rot90(i * z)
# Z = Z.reshape(1,n*n)

U = X * Y +X
V =  (Y **2 - X**2)+Y
# W = Z + Z

# print(X.size, U.size, Y.size, V.size)
# print(X.shape, X[0][1])

# for i in range(0, n * n, 1):
#     # print(i)
#     plt.plot( [ X[0][i],U[0][i] ],[ Y[0][i],V[0][i] ],'k', lw = 1)       #p[x1,x2,....xn], q[y1,y2....yn]
#     # ax1.plot([ X[0][i],U[0][i] ],[ Y[0][i],V[0][i] ], [Z[0][i],W[0][i]], 'r', lw=1)  # a vector

# plt.quiver(X,Y,U,V)
plt.grid()
# plt.axis([-g * 2, g * 2, -g * 2, g * 2], 'equal')
# ax1.plot([0, a[0]], [0, a[1]], [0, a[2]], 'r', lw=3)  # a vector
plt.show()









