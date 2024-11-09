import matplotlib.pyplot as pt
import numpy as np

#First Plot
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

font1 = {'family':'Times', 'color':'blue', 'size':10}
font2 = {'family':'serif', 'color':'green', 'size':7, 'weight':'bold', 'style':'italic'}
pt.subplot(2,2,1)
pt.plot(x, y, color='red', marker='*', ms=3, mfc='pink', mec='black')
pt.title('Sin Curve', fontdict=font1, loc='center')
pt.xlabel('X-Axis', fontdict=font2)
pt.ylabel('Y-Axis', fontdict=font2)
pt.grid(axis='x', ls='--', lw=0.5, color='lightgreen')
pt.grid(axis='y', ls='-.', lw=0.5, color='skyblue')

#Second Plot
x = np.linspace(0, 4*np.pi, 100)
y = np.cos(x)
font1 = {'family':'Times', 'color':'gray', 'size':10}
font2 = {'family':'serif', 'color':'green', 'size':7, 'weight':'bold', 'style':'italic'}
pt.subplot(2,2,2)
pt.plot(x, y, color='red', marker='*', ms=3, mfc='pink', mec='black')
pt.title('Sin Curve', fontdict=font1, loc='center')
pt.xlabel('X-Axis', fontdict=font2)
pt.ylabel('Y-Axis', fontdict=font2)
pt.grid(axis='x', ls='--', lw=0.5, color='lightgreen')
pt.grid(axis='y', ls='-.', lw=0.5, color='skyblue')

#Third Plot
x = np.linspace(0, 4*np.pi, 100)
y = np.tan(x)
font1 = {'family':'Times', 'color':'red', 'size':10}
font2 = {'family':'serif', 'color':'green', 'size':7, 'weight':'bold', 'style':'italic'}
pt.subplot(2,2,3)
pt.plot(x, y, color='red', marker='*', ms=3, mfc='pink', mec='black')
pt.title('Sin Curve', fontdict=font1, loc='center')
pt.xlabel('X-Axis', fontdict=font2)
pt.ylabel('Y-Axis', fontdict=font2)
pt.grid(axis='x', ls='--', lw=0.5, color='lightgreen')
pt.grid(axis='y', ls='-.', lw=0.5, color='skyblue')

#Fourth Plot
x = np.linspace(0, 4*np.pi, 100)
y = np.cos(x)/np.sin(x)
font1 = {'family':'Times', 'color':'magenta', 'size':10}
font2 = {'family':'serif', 'color':'green', 'size':7, 'weight':'bold', 'style':'italic'}
pt.subplot(2,2,4)
pt.plot(x, y, color='red', marker='*', ms=3, mfc='pink', mec='black')
pt.title('Sin Curve', fontdict=font1, loc='center')
pt.xlabel('X-Axis', fontdict=font2)
pt.ylabel('Y-Axis', fontdict=font2)
pt.grid(axis='x', ls='--', lw=0.5, color='lightgreen')
pt.grid(axis='y', ls='-.', lw=0.5, color='skyblue')

pt.subplots_adjust(wspace=0.5, hspace=0.5)
pt.show()

