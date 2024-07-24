import csv

with open("TD.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("----------")

with open("TD.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], row[1], sep=" | ")