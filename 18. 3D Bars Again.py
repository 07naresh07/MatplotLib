import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

x = np.sort(np.array([2, 4, 6, 3, 7, 9, 8]))
y = np.sort(np.array([4, 6, 2, 3, 8, 1, 5]))
font1 = {'family':'Times New Roman', 'size':15, 'color':'Red', 'style':'italic', 'weight':'bold'}
font2 = {'family': 'sherif', 'size':10, 'color':'green', 'style':'oblique','weight':'bold'}

#x, y = np.meshgrid(x,y)
z = np.zeros_like(x)

dx = dy = 0.5
height = np.random.rand(7)

fig = pt.figure(figsize=(10,10))
plot = fig.add_subplot(111, projection='3d')

plot.bar3d(x, y, z, dx, dy, height, color='hotpink')

pt.title('3D Bar Plots', fontdict=font1)
plot.set_xlabel('X-Axis', fontdict=font2)
plot.set_ylabel('Y-Axis', fontdict=font2)

pt.show()
