import numpy as np
import matplotlib.pyplot as plt

X = list()
with open('dataset_anos.txt', 'rt') as reader:
    for point in reader:
        X.append(np.asarray(point.split(",")))

colors = ["r.", "g.", "b."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[0])
plt.show()
