import os
import csv

csvpath = os.path.join("..", "C:/Users/quinn/AppData/Local/Programs/Python/Python37-32", "election_data.csv")

csvRows = []

csvFileObj = open("election_data.csv")
csvreader = csv.reader(csvFileObj)

for row in csvreader:
    Number_of_Votes = len(list(csvreader))
    print(Number_of_Votes)

