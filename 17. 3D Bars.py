import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 2, 3, 4, 5, 6])
x, y = np.meshgrid(x, y)
z = np.zeros_like(x)


fig = pt.figure(figsize=(12, 8))
graph = fig.add_subplot(111, projection='3d')
height = np.random.rand(6, 6)
dx = dy = 0.5
graph.bar3d(x.ravel(), y.ravel(), z.ravel(), dx, dy, height.ravel(), color='r')

graph.set_xlabel('X-Axis')
graph.set_ylabel('Y-Axis')
graph.set_zlabel('Z-Axis')
graph.set_title('3D Plots')

pt.show()