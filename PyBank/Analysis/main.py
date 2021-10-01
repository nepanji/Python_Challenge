# Import CSV cmdlet to create custom objects from the items in the CSV file to make parsing info easier.
import csv
# Import os cmdlet to navigate the file system to look up anc change file variables 
import os

# Create an os independent file path to read the csv file
csvpath = os.path.join('..','Resources','budget_data.csv')
with open(csvpath,'r') as file:
    lines = file.read()
    print(lines)
    print(type(lines))


