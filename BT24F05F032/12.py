import csv

# Open the CSV file
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    
    # Loop through rows
    for row in reader:
        print(row)   # Each row is a list of values
