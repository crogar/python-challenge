import os
import csv

print(os.getcwd())
#reference to budget_data in ./Resources/budget_data.cs
budget_data = os.path.join(os.getcwd(),'Resources/budget_data.csv')

#Declaring variables to store the data from the CSV file
data = []
net_total = 0


def sumatory(x): 
    ''' This function receives a list containing Profit/Losses will add them up
        it will return the net total amount
    '''
    return sum([x[1] for x in data])

with open(budget_data, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append([row['Date'], float(row['Profit/Losses'])])

# obtaining The total number of months included in the dataset
# obtaining The net total amount of "Profit/Losses" over the entire period

net_total = sumatory(data)
print(f"Total: {net_total}")

# 




