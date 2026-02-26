import csv
with open("p202_pets.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Only print the names
with open("p202_pets.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])