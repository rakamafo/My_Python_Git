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
    file_data = open('rotation_matrix_3D_demo.txt', 'r').read()        # read the file, associate with a file pointer/ object
    # print(file_data)
    lines = file_data.split('\n')       ## read all lines, split with \n and store in a list
    roll = lines[0].split(':')          # lines[0] stores 1st line in file. roll becomes a list, split by :
    pitch = lines[1].split(':')
    yaw = lines[2].split(':')


    phi = float(roll[1])    # phi is the 2nd value in te roll list, this a string and is converted to float
    theta = float(pitch[1])
    psi = float(yaw[1])

    # Moving Frame
    f = 5
    frame_x = np.array([f,0,0])
    frame_y = np.array([0,f,0])
    frame_z = np.array([0,0,f])

    # vector = np.array([2,5,0])  # input arbitary vector/ point.
    # t = rotate_z(psi,vector)    # cal new position and return vector

    ax1.clear()     # clears the plot every iteration
    # Setting the axes properties
    ax1.set_xlim3d([-10.0, 10.0])
    ax1.set_xlabel('X')
    ax1.set_ylim3d([-10.0, 10.0])
    ax1.set_ylabel('Y')
    ax1.set_zlim3d([-10.0, 10.0])
    ax1.set_zlabel('Z')
    ax1.set_title('3D Test')

    # PLot Origin and Axis.
    l = 10      # length of the axis.
    ax1.plot([0, l], [0, 0], [0, 0], 'r', lw=1)  # X axis
    ax1.plot([0, 0], [0, l], [0, 0], 'g', lw=1)  # Y axis
    ax1.plot([0, 0], [0, 0], [0, l], 'b', lw=1)  # Z axis

    # ax1.plot([0,vector[0]],[0,vector[1]], [0,0],'b')       # plot input arbitary vector
    # ax1.plot([0, t[0]], [0, t[1]], [0,0], 'r')              # plot repositioned vector
    ax1.plot([0,frame_x[0]],[0, frame_x[1]],[0, frame_x[2]],'k', lw = 2)
    ax1.plot([0,frame_y[0]],[0, frame_y[1]],[0, frame_y[2]],'m', lw = 2)
    ax1.plot([0,frame_z[0]],[0, frame_z[1]],[0, frame_z[2]],'y', lw = 2)

    frame_x = rotate_mat(phi, theta, psi, frame_x)
    frame_y = rotate_mat(phi, theta, psi, frame_y)
    frame_z = rotate_mat(phi, theta, psi, frame_z)

    ax1.plot([0,frame_x[0]],[0, frame_x[1]],[0, frame_x[2]],'k', lw = 3)
    ax1.plot([0,frame_y[0]],[0, frame_y[1]],[0, frame_y[2]],'m', lw = 3)
    ax1.plot([0,frame_z[0]],[0, frame_z[1]],[0, frame_z[2]],'y', lw = 3)


def rotate_mat(phi, theta, psi, v):

    phi_rad = phi * np.pi/180.0
    theta_rad = theta * np.pi/180.0
    psi_rad = psi * np.pi/180.0       # convert deg to radians.

    mat_x = np.array([[1,               0,                 0],
                      [0, np.cos(phi_rad), - np.sin(phi_rad)],
                      [0, np.sin(phi_rad),   np.cos(phi_rad)] ])

    mat_y = np.array([[np.cos(theta_rad),  0, np.sin(theta_rad)],
                      [0,                  1,                 0],
                      [-np.sin(theta_rad), 0, np.cos(theta_rad)]])

    mat_z = np.array([[np.cos(psi_rad), - np.sin(psi_rad),  0],
                      [np.sin(psi_rad),   np.cos(psi_rad),  0],
                      [0              ,                 0,  1]])

    #  Matrix mul of Yaw * (pitch * roll), note the order of multiplication.
    # m = np.matmul(np.matmul(mat_z, np.matmul(mat_x,mat_y)) , v)    # perform mat mul
    m = np.matmul(np.matmul(mat_z, np.matmul(mat_y, mat_x)), v)    # perform mat mul, correct order !
    # print(m)
    return m

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()












