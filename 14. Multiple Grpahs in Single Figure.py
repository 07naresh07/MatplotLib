import matplotlib.pyplot as pt
import numpy as np

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
fig = pt.figure()
fig.patch.set_facecolor('skyblue')
graph =  fig.add_subplot(2,2,1, facecolor='lightblue', alpha=0.2)
graph.plot(x, y, marker='*', ms=5, color='red', mfc='y', mec='magenta')
graph.spines['top'].set_color('white')
graph.spines['left'].set_color('white')
graph.spines['bottom'].set_color('white')
graph.spines['right'].set_color('white')

graph.tick_params(axis='x', color='white', size=8)
graph.tick_params(axis='y', color='white', size=8)
graph.set_title('sin Plot', size=13, style='italic')
graph.set_xlabel('X-Axis', color='blue')
graph.set_ylabel('Y-Axis', color='blue')

x = np.linspace(0, 4*np.pi, 100)
y = np.cos(x)
graph = fig.add_subplot(2,2,2, facecolor='lightblue', alpha=0.5)
graph.plot(x,y, color='black', marker='D', ms=2, mfc='white', mec='black')

graph.spines['top'].set_color('green')
graph.spines['left'].set_color('green')
graph.spines['bottom'].set_color('green')
graph.spines['right'].set_color('green')

graph.tick_params(axis='x', color='white', size=8)
graph.tick_params(axis='y', color='white', size=8)
graph.set_title('cos Plot', size=13, style='italic')
graph.set_xlabel('X-Axis', color='blue')
graph.set_ylabel('Y-Axis', color='blue')

x = np.linspace(0, 4*np.pi, 100)
y = np.tan(x)
graph = fig.add_subplot(2,1,2, facecolor='cyan', alpha=0.5)
graph.plot(x,y, color='black', marker='D', ms=2, mfc='white', mec='black')

graph.spines['top'].set_color('green')
graph.spines['left'].set_color('green')
graph.spines['bottom'].set_color('green')
graph.spines['right'].set_color('green')

graph.tick_params(axis='x', color='white', size=8)
graph.tick_params(axis='y', color='white', size=8)
graph.set_title('tan Plot', size=13, style='italic')
graph.set_xlabel('X-Axis', color='blue')
graph.set_ylabel('Y-Axis', color='blue')

pt.subplots_adjust(hspace=0.5, wspace=0.5)
pt.suptitle('Trigonometric Function Plots', color='red', size=15)


pt.show()