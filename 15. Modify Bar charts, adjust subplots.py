import matplotlib.pyplot as pt
import numpy as np

names = ['Tree', 'Dog', 'Ball', 'Sugar', 'Daddy', 'Hot']
bars = np.arange(6)+5
pt.barh(bars, (5, 6, 7, 4, 9, 2), color = 'red', height = 0.5)

pt.xlabel('Height of the Objects', c='deeppink')
pt.ylabel('No of Objects', c='deeppink')
pt.title('Height and Number of objects Plot', c='blue')

pt.tick_params(axis='x', color='green', size=5)
pt.tick_params(axis = 'y', color = 'green', size=5)
pt.yticks(bars, names)

pt.subplots_adjust(top=0.90, bottom=0.13, left=0.15, right=0.92, wspace=0.25, hspace=0.25)
pt.show()
