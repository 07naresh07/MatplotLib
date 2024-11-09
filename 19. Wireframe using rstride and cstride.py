import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = pt.figure(figsize=(10,8))
chart = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data(0.05)
chart.plot_wireframe(x, y, z, rstride=10, cstride=10)

pt.show()