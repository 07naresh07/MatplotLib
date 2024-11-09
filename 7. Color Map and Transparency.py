import matplotlib
import matplotlib.pyplot as pt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array([0, 10, 25, 41, 54, 65, 70, 85, 89, 90, 59, 95, 99])
sizes = np.array([6, 10, 13, 14, 12, 13, 11, 15, 13, 14, 11, 12, 17])

pt.scatter(x, y, c=colors, cmap = 'viridis', s=sizes, alpha=0.9)    #alpha is used for transparency of the scattered dots & there are other colormaps than viridis
pt.colorbar()
pt.show()