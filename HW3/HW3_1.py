import matplotlib.pyplot as plt
import csv
/Users/FranciscoP/Desktop/untitled folder/HW3/HW3_1.py
def main():
    with open('BdayCSV.txt', 'rb') as csvfile:
               reader = csv.DictReader(csvfile, delimiter=',')

        reader.next()
        collisions = {}
        time = [row[1] for row in reader]

        for i in time:

            split = i.find(":")
            hour = int(i[:split])
            collisions[hour] = collisions.get(hour,0)+1

        print collisions

    plt.bar(collisions.keys(),collisions.values())
    plt.title("Collisions on January 6, 2015")
    plt.xlabel("Hours")
    plt.xlim(0,23)
    plt.ylabel("Number of Collisions")
    plt.ylim(0,100)

    plt.show()

main()
