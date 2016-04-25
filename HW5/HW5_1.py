
import csv,re
import matplotlib.pyplot as plt
def HW5_1():

    prefix = "nystate/yob"
    suffix = ".txt"
    NumofNames = 0
    NumofYears = []

    years = [i for i in range(1990,2011)]

    for i in years:
        txtName = prefix + str(i) + suffix
        csvfile = open(txtName)
        reader = csv.DictReader(csvfile, fieldnames = ("Name","M/F"))

        for row in reader:
            reSearch = re.search('Er[ick][ich]', row["Name"])

            if reSearch != None:
                NumofNames+=1
        NumofYears.append(NumofNames)

        NumofNames=0

    plt.plot(years, NumofYears)
    plt.title("How often the name Eric was used(various ways it was spelled) over the last 21 years")
    plt.xlabel("Year")
    plt.ylabel("Number of Occurances ")
    plt.axis([1990,2010,0,100])
    plt.show()

HW5_1()