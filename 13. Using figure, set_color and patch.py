import matplotlib
import matplotlib.pyplot as pt
import numpy as np

x = np.array([0, 5, 8, 13, 16])
y = np.array([0, 5, 8, 13, 16])
font = {'family':'Times New Roman', 'fontsize':8, 'color':'white', 'style':'italic', 'weight':'bold'}

fig = pt.figure()
fig.patch.set_facecolor('hotpink')
fig.patch.set_alpha(0.5)
graph = fig.add_subplot(1, 1, 1, facecolor='y', alpha=0.1)
graph.plot(x,y, c='red',lw=3, marker='*', mfc='white', mec='blue',ls='dashed')

graph.spines['top'].set_color('white')
graph.spines['bottom'].set_color('white')
graph.spines['left'].set_color('white')
graph.spines['right'].set_color('white')

graph.tick_params(axis='x', color='white', size=5)
graph.tick_params(axis='y', color = 'white', size=5)
graph.set_title('X vs Y Curve', color='g', style='italic', fontsize=10, weight='bold')
graph.set_xlabel('X-Axis', fontdict=font)
graph.set_ylabel('Y-Axis', fontdict=font)
pt.show()