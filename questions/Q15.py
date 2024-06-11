import csv
f = open("trail.csv", "r")
csv_reader=csv.reader(f)
for i in csv_reader:
    print(','.join(i))
