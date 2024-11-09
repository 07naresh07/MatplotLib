import matplotlib.pyplot as pt
import numpy as np

data = np.array([23, 25, 31, 10, 37, 41])
color=np.array(['violet', 'lightblue', 'lightgreen', 'hotpink', 'crimson', 'hotpink'])
wedges = np.array([0.014, 0.015, 0.018, 0.021, 0.023, 0.015])
label = np.array(['Bike', 'Private Car', 'Public Bus','Bicycle','By Foot', 'others'])
pt.pie(data, explode=wedges, colors=color, startangle=0, shadow=True, labels=label)
pt.title('Pie Chart')
pt.legend(title='Vehicle Used', loc='upper left')
pt.savefig('pie.jpg', dpi=1200)
pt.show()