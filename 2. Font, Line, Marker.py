import matplotlib.pyplot as pt
import numpy as np

x = np.array([0,6])
y = np.array([0,250])
X = [0, 10, 20, 30, 40, 50]
Y = [0, 10, 20, 30, 40, 50]
pt.plot(x, y, 'g', linestyle="-.", marker='D',ms=6, mec='r', mfc='hotpink') #ms = MarkerSize, mec = MarkerEdgeColor, mfc=MarkerFaceColor
pt.plot(X, Y, ls="dashed", lw=2, c='r', marker='P', markersize=4, markeredgecolor='b',markerfacecolor='w')
pt.xlabel("X-Axis", color='pink')
pt.ylabel("Y-Axis",color='pink')
pt.title("Graph Comparision", c='b',fontsize='20')
pt.show()