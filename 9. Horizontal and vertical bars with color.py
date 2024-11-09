import matplotlib
import matplotlib.pyplot as pt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([5, 7, 2, 15])
pt.subplot(1,2,1)
colors = np.array(['#FF1493', '#DC143C', '#8B008B','#6495ED']) # color with hexdecimal value
pt.bar(x, y, color=colors, alpha=0.8, width=0.5)  #bar width=0.8 default

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
pt.subplot(1,2,2)
colors = np.array(['cyan', 'green', 'violet', 'hotpink'])
pt.barh(x,y, height=0.3, color=colors)    #use height instead of width in horizontal curve

pt.show()