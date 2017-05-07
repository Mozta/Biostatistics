import numpy as np
import matplotlib.pyplot as plt

x = list()
y = list()

with open('dataset_anos.txt', 'rt') as reader:
    for point in reader:
        x.append(int(point.split(",")[0]))
        y.append(float(point.split(",")[1]))

plt.plot(x,y)
plt.show()
