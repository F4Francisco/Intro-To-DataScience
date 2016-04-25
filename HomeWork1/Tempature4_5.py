#Francisco Perez, Spring 2016

#historical min temperature for January 2016

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
def scale(mins, plt, lab,col):
     """
     Takes a list, label, and color and creates a scatter plot
     of the percentage change with respect to the first entry
     in the list.
     """
     baseNum = mins[0]
     scaled= [i*100/baseNum-100 for i in mins]
     plt.scatter(days, scaled, label=lab, c = col, s=75)
     #scale(mins,plt,'Min", "blue") 
     



def main():
     #The url is made up of the prefix, year, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/1/"
     suffix = "/DailyHistory"
     days = []          #Sets up a list to store days
     mins = []           #Sets up a list to store min values
     for day in range(1,32): #For each year
          days.append(day)       #Add the year to the list
          url = prefix+str(day)+suffix      #Make the url
          Min = getTempFromWeb("Min",url)
          
          mins.append(Min)
          print "January:",day,
          
          avg = sum (mins) /31dxyty
          print avg
     plt.plot(days, mins, color='b', label="Min Temp")     #Plot min as blue
     plt.title("The  Min Tempatures for January 2016 In NYC")       #Title for plot
     plt.xlabel('Days')                     #Label for x-axis
     plt.ylabel('Degrees')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()


main()
