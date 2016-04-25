from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

m = Basemap(projection='mill', llcrnrlat=39, urcrnrlat=43, \
            llcrnrlon=-75, urcrnrlon=-72, resolution='c')
m.readshapefile("st99_d00", "NYCMAP", drawbounds= True )
m.drawcoastlines()
m.drawcountries()

m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

with open('Crashes.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    lat = [float(row[3]) for row in reader]


    with open('Crashes.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        lon  = [float(row[4]) for row in reader]

        with open('NYCCrashes.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()
            lat2 = [float(row[4]) for row in reader]
            print lat2
            with open('NYCCrashes.csv', 'rb') as csvfile:
                reader = csv.reader(csvfile)
                reader.next()
                lon2 = [float(row[5]) for row in reader]
                print lon2
#lat =40.8317974,40.8378662,40.8357171,40.84013,40.8386213,40.8425139
#lon =-73.8889361,-73.8635562,-73.8920447,-73.8802991,-73.8811366,-73.871534

x, y = m((lon),(lat))
m.plot(x, y, 'ro', markersize=10, alpha=.7)

x,y = m(lon2,lat2)
m.plot(x,y,'go',markersize=5,alpha=.6)

plt.title('NYC Crashes Red = 10460 zip, Green = All')
plt.show()
