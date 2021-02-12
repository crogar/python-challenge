import os,csv
from collections import namedtuple

budget_data = os.path.join(os.getcwd(),'Resources/budget_data.csv') #reference to budget_data in ./Resources/budget_data.cs
analysis_output = os.path.join(os.getcwd(),'Analysis/analysis.txt')
#Declaring variables to store the data from the CSV file
data = []
print_out = []
months = namedtuple("months","Date profit_losses")  # using namedtuple to keep list organized 

def summation(data_set): 
    ''' This function receives a list containing Profit/Losses, it will add them up.
        It will return the net total amount using index 1 to locate that data
    '''
    return sum([month.profit_losses for month in data_set])

def calc_changes(data_,mode='average'):
    ''' This function receives a list containing Profit/Losses will add them up
        it will return the the average, max or min based on the chosen mode "average","GRI", or "GRD"
    '''
    changes = []
    for i in range(0,len(data_)-1):
        change = data_[i+1].profit_losses- data_[i].profit_losses 
        changes.append((data_[i+1].Date,change))   # first Element in tuple is the month and second element is the actual change
    if mode == 'average':
        average_change = sum([x[1] for x in changes]) / len(changes)
        return round(average_change,2)
    elif  mode == 'GRI':
        return max(changes, key = lambda i: i[1])  # using Lambda function to tell MAX to use The second element in tuple as comparison 
    elif mode == 'GRD':
        return min (changes, key = lambda i: i[1]) # using Lambda function to tell MIN to use The second element in tuple as comparison 
    else:
        raise ValueError(f"{mode} is not a supported parameter") # if user doesn't provide a valid mode, we raise a ValueError
    
def main():
    with open(budget_data, newline='') as csvfile: # reading CSV File and storing the rows into a list
        reader = csv.DictReader(csvfile)
        for row in reader:
            month = months(row['Date'], float(row['Profit/Losses']))  # appending month of type months(namedTuple)
            data.append(month)

    print_out.append("Financial Analysis")
    print_out.append("----------------------------")
    # obtaining The total number of months included in the dataset
    print_out.append(f"Total Months: {len(data)}")
    # obtaining The net total amount of "Profit/Losses" over the entire period
    net_total = summation(data)
    print_out.append(f"Total: ${net_total}")
    # Calculates the changes in "Profit/Losses" over the entire period, then returns the average of those changes
    average_change = calc_changes(data, mode='average')
    print_out.append(f'Average Change: ${average_change}')
    # Calculates The greatest increase in profits (date and amount) over the entire period
    GRI = calc_changes(data,mode="GRI")    # Receiving a tuple containing the month and the GRI change i.e ('Sep-2016', -665765.0)
    print_out.append(f'Greatest Increase in Profits: {GRI[0]} (${GRI[1]})')
    # calculates The greatest decrease in losses (date and amount) over the entire period
    GRD = calc_changes(data,mode="GRD")    # Receiving a tuple containing the month and the GRD change i.e ('Sep-2016', -665765.0)
    print_out.append(f'Greatest Decrease in Profits: {GRD[0]} (${GRD[1]})')

    with open(analysis_output, 'w', newline='') as out_file:  # Generating analysis.txt printing out same result as in the console
        for line in print_out:
            print(line)
            out_file.write(line + '\n') # using escape code \n so this way python will add a new line after wrinting a new row

if __name__ == '__main__':
    main()