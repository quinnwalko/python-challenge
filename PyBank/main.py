import os
import csv

csvpath = os.path.join("..", "C:/Users/quinn/AppData/Local/Programs/Python/Python37-32", "budget_data.csv")

csvRows = []

csvFileObj = open("budget_data.csv")
csvreader = csv.reader(csvFileObj)
for row in csvreader:
    if csvreader.line_num == 1:
        continue
    csvRows.append(row)
    
    Number_of_Rows = len(list(csvreader))
    print(Number_of_Rows)
    
with open("budget_data.csv") as csv_file:
    csvreader = csv.DictReader(csv_file)
    total = sum(float(row["Profit/Losses"]) for row in csvreader)
print(total)
    
    
    
    
