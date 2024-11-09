import matplotlib.pyplot as pt
import numpy as np

x = np.random.randint(100,200,100)
y = np.random.randint(150, 300, 100)
size = 10*np.random.randint(50, 100, 100)
colors = np.random.randint(100, size=100)

pt.scatter(x, y, c=colors, s=size, cmap='gist_rainbow_r', alpha=0.5)
pt.colorbar()


pt.show()