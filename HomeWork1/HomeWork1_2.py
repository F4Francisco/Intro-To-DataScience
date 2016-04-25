#Francisco Perez, Spring 2016
#Uses multiple files from weather underground to graph
#    historical max temperatures.

#The libraries to plot, load webpages, and use regular expressions
import matplotlib.pyplot as plt
import urllib2
import re


#A function that takes the kind of temperature ("Max", "Min", "Ave") and
#a URL and returns the temperature from that line.
def getTempFromWeb(kind,url):
     page = urllib2.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].find(kind+" Temperature") >= 0:
               m = i
     searchObj = re.search('\d+', lines[m+2])
     return int(searchObj.group(0))


def main():
     #The url is made up of the prefix, year, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/"
     suffix = "/01/06/DailyHistory"
     years = []          #Sets up a list to store years
     maxs = []           #Sets up a list so store max values
     for year in range(1991,2017): #For each year
          years.append(year)       #Add the year to the list
          url = prefix+str(year)+suffix      #Make the url
          M = getTempFromWeb("Max",url)      #Call the function to extract temp
          maxs.append(M) #Add the temp to the list        
          print year, M
     plt.plot(years, maxs, color='r', label="Max Temp")     #Plot max as red
     plt.title(" The Max Tempatures in NYC for January 6 Over the last 25 Years")       #Title for plot
     plt.xlabel('Years')                     #Label for x-axis
     plt.ylabel('Degrees')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()

 
     print "The list of max values is: ", maxs

main()
