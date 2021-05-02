import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)        # for 2d Plotting
ax1 = p3.Axes3D(fig)       # for 3D plotting


def animate(i):
    file_data = open('rotation_matrix_demo.txt', 'r').read()        # read the file, associate with a file pointer/ object
    # print(file_data)
    lines = file_data.split('\n')       ## read all lines, split with \n and store in a list
    roll = lines[0].split(':')          # lines[0] stores 1st line in file. roll becomes a list, split by :
    pitch = lines[1].split(':')
    yaw = lines[2].split(':')

    # print(roll[1])
    # print(pitch[1])
    # print([1])

    phi = float(roll[1])    # phi is the 2nd value in te roll list, this a string and is converted to float
    theta = float(pitch[1])
    psi = float(yaw[1])

    # print(phi,'  ',theta,'  ',psi, type(phi))
    vector = np.array([2,5,0])  # input arbitary vector/ point.
    t = rotate_z(psi,vector)    # cal new position and return vector

    ax1.clear()     # clears the plot every iteration
    ax1.plot([0,vector[0]],[0,vector[1]], [0,0],'b')       # plot input arbitary vector
    ax1.plot([0, t[0]], [0, t[1]], [0,0], 'r')              # plot repositioned vector
    # ax1.set_aspect('equal', 'box')                  # make the axis equal
    # ax1.axis([-10,10,-10,10])                       # set limits on axis.


    # Setting the axes properties
    ax1.set_xlim3d([-10.0, 10.0])
    ax1.set_xlabel('X')
    ax1.set_ylim3d([-10.0, 10.0])
    ax1.set_ylabel('Y')
    ax1.set_zlim3d([-10.0, 10.0])
    ax1.set_zlabel('Z')
    ax1.set_title('3D Test')




def rotate_z(psi, v):
    psi_d = psi * np.pi/180.0       # convert deg to radians.
    mat_z = np.array([[np.cos(psi_d), - np.sin(psi_d),  0],
                      [np.sin(psi_d),   np.cos(psi_d),  0],
                      [0            ,               0,  1]])
    m = np.matmul(mat_z,v)      # perform mat mul

    print(m)
    return m



ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()












