import matplotlib.pyplot as plt
import csv

def main():
    date = []
    with open('ZipCodeCSV.txt', 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            date.append(row["DATE"])

    month = []
    for dates in range(len(date)):
        split = date[dates].split("/")
        month.append(int(dates[0]))

    plt.hist(month)
    plt.title("Collisions in the Zip Code Area 10460 over the last year")
    plt.xlabel("Months")
    plt.xlim(1,12)
    plt.ylabel("Number of Collisions")
    plt.show()
main()