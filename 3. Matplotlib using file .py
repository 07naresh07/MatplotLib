import matplotlib
import matplotlib.pyplot as pt

x = []
y = []

with open("input_file.txt", 'r') as file:
    data = file.read().split("\n")
    print(data, "\n")

    for i in data:
        datas = i.split(',')
        print(datas)
        x.append(datas[0])
        y.append(datas[1])

print(x, y)
pt.plot(x, y)
pt.title("X and Y Plot")
pt.xlabel("X-Axis")
pt.ylabel("Y-Axis")
pt.show()



