import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2+Y**2))+np.cos(np.cos(X**2+Y**2))

fig = pt.figure(facecolor='hotpink', figsize=(10,8))
chart = fig.add_subplot(111, projection='3d')
chart.set_facecolor('lightgreen')
chart.set_alpha(0.5)
chart.plot_wireframe(X,Y,Z, rstride=2, cstride=2)

pt.show()