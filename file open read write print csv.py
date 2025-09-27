import csv

with open("data.csv") as csv_file:      # Default mode is read mode therefore "r" can be considered redundant as in the next block
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

print(" ")

with open("data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

print(" ")

with open("data.csv") as csv_file:      # This method reads the entire file as a single string & is less efficient
    for row in csv_file:
        print(row)

print(" ")

with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Kamran", "33"])        # This will not only add new data to the file but will overwrite all previous data

with open("data.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)