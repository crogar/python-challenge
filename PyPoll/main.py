import os
import csv
from collections import defaultdict,namedtuple

#reference to budget_data in ./Resources/budget_data.cs
election_data = os.path.join(os.getcwd(),'Resources/election_data.csv')
analysis = os.path.join(os.getcwd(),'Analysis/analysis.txt')
#Declaring variables to store the data from the CSV file
dataset = []
print_out = []
votes = namedtuple("votes","Voter_ID County Candidate")  # using namedtuple to keep list organized 

def analysis_dataset(data_set):
    candidates = defaultdict(lambda: 0)
    print_out.append("Election Results")
    print_out.append('-------------------------')    
    # using defaultdict allows to count the votes for each candidate without having to worry about the initial value
    for candidate in data_set:
        candidates[candidate.Candidate] += 1
    # sorting Dict out based on Votes 
    candidates = dict(sorted(candidates.items(),key=lambda i: i[1], reverse=True))
    # The total number of votes cast
    total_votes = len(data_set)
    print_out.append(f"Total Votes: {total_votes}")
    print_out.append('-------------------------')
    for k,v in candidates.items():
        # The percentage of votes each candidate won
        percentage = "{0:.3f}%".format((v/total_votes)*100)
        print_out.append(f"{k}: {percentage} ({v})")
    print_out.append('-------------------------')      
    # The winner of the election based on popular vote. 
    # using nex(iter()) to get the first candidate in the dict, this because we previously sorted it!!!
    print_out.append(f"Winner: {next(iter(candidates.keys()))}") 
    print_out.append('-------------------------')     
    for line in print_out:
        print(line)
    # exports a text file with the results.
    with open(analysis, 'w+') as out_file:  # Generating analysis.txt printing out same result as in the console
        for line in print_out:
            line = line + "\n"
            out_file.write(line)

def main():
    with open(election_data, newline='') as csvfile: # reading CSV File and storing the rows into a list
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote = votes(row['Voter ID'], row['County'], row['Candidate'])  # appending canditate of type Candidates(namedTuple)
            dataset.append(vote)
    # A complete list of candidates who received votes
    analysis_dataset(dataset)

if __name__ == '__main__':
    main()