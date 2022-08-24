import csv

dataset_1 = []
dataset_2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("arcgivedata.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)