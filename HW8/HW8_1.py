from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

m = Basemap(projection='mill',llcrnrlat=39,urcrnrlat=43,\
            llcrnrlon=-75,urcrnrlon=-72,resolution='c')
m.readshapefile("st99_d00", "NYCMAP", drawbounds= True )
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')


with open('CUNY.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    lon = [float(row[2]) for row in reader]
    print lon


    with open('CUNY.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        lat = [float(row[1]) for row in reader]
    print lat


''''
f = open('CUNY.txt')
csv_f = csv.reader(f)
for row in csv_f:
    print (row[2])
   # print Longitude
f.close()
f = open('CUNY.txt')
csv_f = csv.reader(f)
for row in csv_f:
    print (row[1])
    #print Latitude
f.close()
'''
#at = 40.740977, 40.717367, 40.856673, 40.630276, 40.630276, 40.747639, 40.752846, 40.817828, 40.768731, 40.769939, 40.578349, 40.743951,40.873442,40.66624,40.695507,40.744988,40.736316,40.755343,40.748151,40.819548,40.748724,40.702821,
##on = -73.984252,-74.012178, -73.910127,-73.955545,-74.153563,-73.943676,-73.984133,-73.926862, -73.964915,-73.986469,-73.934465,-73.935154,-73.889361,-73.957349, -73.987882,-73.816444,-73.820035,-73.988846,-73.989723,-73.949518,-73.984205,-73.795776

x, y = m(lon,lat)
m.plot(x, y, 'ro', markersize=10, alpha=.5)

plt.title('CUNY Campus Plotting')
plt.show()

