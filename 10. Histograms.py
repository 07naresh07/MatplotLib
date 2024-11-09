import matplotlib
import matplotlib.pyplot as pt
import numpy as np

height_data = np.random.normal(170, 10, 100)
pt.hist(height_data, color = 'deeppink', alpha=0.6)

pt.show()
