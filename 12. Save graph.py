import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as pt
import numpy as np

x = np.random.randint(50, size=50)
y = np.random.randint(40, size=50)
colors = np.random.randint(100, size=50)
sizes = 10*np.random.randint(100, size=50)

pt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap = 'nipy_spectral_r')
pt.colorbar()
plt.savefig('graph.jpg', dpi=600)
pt.show()
