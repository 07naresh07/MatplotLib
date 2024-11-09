import matplotlib
import matplotlib.pyplot as pt
import numpy as np

x = np.linspace(0, 4 * np.pi, 100)
y=np.sin(x)

font1 = {'family':'Times New Roman','color':'hotpink','size':15}
font2 = {'family':'serif','color':'lightblue','fontsize':10}
pt.plot(x, y, c='lightgreen', lw='3',ls='-.')
pt.title("Sine Wave Curve", fontdict=font1, loc='left') #default loc is 'center
pt.xlabel("X-Axis", fontdict=font2)
pt.ylabel("Y-Axis", fontdict=font2)
pt.grid(axis='x', color='lightgray',ls='dotted',lw='2') #to choose which axis grid to use
pt.grid(axis='y', color='darkgray',ls='dotted',lw='2')
pt.show()