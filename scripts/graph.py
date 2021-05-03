import matplotlib.pylab as plt
import json
from os import listdir
from os.path import isfile, join

path="./data"
files = [f for f in listdir(path) if isfile(join(path, f))]

points = {}
for file in files:
    with open(path + "/" + file, 'r') as reader:
        data = json.load(reader)
        if "end" in data and "sum_received" in data["end"]:
            xval = int(file[:-5])/1000
            yval = data["end"]["sum_received"]["bits_per_second"]
            points[xval] = yval

sortedPoints = sorted(points.items())
x, y = zip(*sortedPoints)
plt.plot(x,y)
plt.xlabel("Period (s)")
plt.ylabel("Average bit per second throughput")
plt.savefig('figure4.pdf')
