import os
import csv

#Locating correct file path
csvpath = os.path.join('budget_data.csv')

#Initialize variables
totalmonths = []
totalamount = []
amountchange = []

#Open CSV file and store into variable
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f'Financial Analysis'+'\n')
    print(f'---------------------------'+'\n')

#Iterate and append through rows in stored csvfile
    for row in csvreader:
        totalmonths.append(row[0])
        totalamount.append(int(row[1]))

#Iterate through profits in order to get the monthly change
    for amount in range(len(totalamount)-1):
        amountchange.append(totalamount[amount+1]-totalamount[amount])

#Calculate max and min profit change
maxamountchange = max(amountchange)
minamountchange = min(amountchange)

#Calculate max and min dates
maxmonth = amountchange.index(max(amountchange))+1
minmonth = amountchange.index(min(amountchange))+1

print(f"Total Months: {len(totalmonths)}")
print(f"Total Amount: ${sum(totalamount)}")
print(f"Average Change: ${round(sum(amountchange)/len(amountchange),2)}")
print(f"Greatest Increase in Profits: {totalmonths[maxmonth]} (${maxamountchange})")
print(f"Greatest Decrease in Profits: {totalmonths[minmonth]} (${minamountchange})")

