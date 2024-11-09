import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

x = np.array([2, 3, 5, 6])
y = np.array([6, 4, 8, 9])
z = np.array([8, 3, 9, 10])

colors=[0, 20, 50, 80]
fig = pt.figure()
data=fig.add_subplot(111, projection = '3d')
graph=data.scatter(x, y, z, c=colors, marker='o', cmap='viridis')  #or we can use : data.plot3D(x,y,z) or data.scatter(x,y,z) or data.plot(x,y,z)
data.set_xlabel("X-Axis", color = 'red')
data.set_ylabel('Y-Axis', color='blue')
data.set_zlabel('Z-Axis', color='pink')
fig.colorbar(graph)
pt.show()