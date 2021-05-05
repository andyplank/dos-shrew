import matplotlib.pylab as plt
from os import listdir
from os.path import isfile, join

points = {}
with open("res.txt", 'r') as reader:
    while True:
        x = reader.readline()
        if not x:
            break
        y = reader.readline()
        if not y:
            break
        x = int(x[:-3])
        y = float(y[:-5])
        points[x] = y

sortedPoints = sorted(points.items())
x, y = zip(*sortedPoints)
plt.plot(x,y)
plt.xlabel("Period (ms)")
plt.ylabel("Average KBps throughput")
plt.savefig('Results.pdf')
