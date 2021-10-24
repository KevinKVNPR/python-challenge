import os
import csv
from typing import Text

#paths to csv
os.chdir(os.path.dirname(os.path.realpath(__file__)))
bank_data_cvs= os.path.join("Resources", "budget_data.csv")
#reads csv
with open(bank_data_cvs, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
file = open(bank_data_cvs)
reader = csv.reader(file)
header = next(reader)

# Constants
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]
total_revenue = 0
DATE_COL = 0
REVENUE_COL = 1
# Calcuating the number of months, and total renevue in the period. 
for row in reader:
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[REVENUE_COL])
# Greatest increase and decrease. 
    revenue_change = int(row[REVENUE_COL]) - prev_revenue
    prev_revenue = int(row[REVENUE_COL])
    revenue_change_list = revenue_change_list + [revenue_change]
    month_of_change = month_of_change + [row[DATE_COL]]

    if (revenue_change > greatest_increase[1]):
        greatest_increase[0] = row[DATE_COL]
        greatest_increase[1] = revenue_change
    
    if (revenue_change < greatest_decrease [1]):
        greatest_decrease[0] = row[DATE_COL]
        greatest_decrease[1] = revenue_change
# Calculating the average change. 
    revenue_avg = sum(revenue_change_list) / total_months

#Print out Data:
output =(
"\nFinancial Analysis\n"
"\n-------------------\n"
f"Total Months:  {total_months}\n"
f"Total Revenue: {total_revenue}\n"
f"Average  Change: {revenue_avg}\n"
f"Greatest Increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
f"Greatest Decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)
print(output)

# open the output file, create a header row, and then write the text file
file_output = os.path.join("financial_analysis.txt")
with open(file_output, "w") as textfile:
    textfile.write(output)

   