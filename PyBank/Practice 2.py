import os
import csv

#Locating correct file path
csvpath = os.path.join('budget_data.csv')

#Initialize variables
totalmonths = 0
totalamount = 0
lastamount = 0
monthchange = []

#Reading the correct file path above
with open(csvpath) as csvfile: 
    reader = csv.DictReader(csvfile)
    print(f'Financial Analysis'+'\n')
    print(f'---------------------------'+'\n')

    
    for row in reader:

        #Iterating through the list while adding months and columns
        totalmonths = totalmonths + 1
        totalamount = totalamount + int(row["Profit/Losses"])

        #Calculating value change and month
        totalvaluechange = int(row["Profit/Losses"]) - lastamount
        lastamount = int(row["Profit/Losses"])
        monthchange = monthchange + row["Date"]





        print(row[monthchange])
        
        
        #print(row["Profit/Losses"])



"""
print(f"Total Months: {totalmonths}")
print(f"Total Amount: ${totalamount}")
"""




    



