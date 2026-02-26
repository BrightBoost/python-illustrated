import csv

with open("p202_pets.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Species", "Age"])
    writer.writerow(["Zia", "Cat", "1"])
    writer.writerow(["Wiesje", "Dog", "7"])