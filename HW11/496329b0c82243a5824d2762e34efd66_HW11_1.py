from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
import csv

with open('CUNY.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    lon = [float(row[2]) for row in reader]
    print (lon)


    with open('CUNY.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        lat = [float(row[1]) for row in reader]
    print (lat)

    loc = zip(lon,lat)

print loc
points = np.array(loc)
print points
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
