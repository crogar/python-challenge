import os
import csv
from collections import defaultdict,namedtuple

#reference to budget_data in ./Resources/budget_data.cs
election_data = os.path.join(os.getcwd(),'Resources/election_data.csv')
analysis = os.path.join(os.getcwd(),'Analysis/analysis.txt')
#Declaring variables to store the data from the CSV file
dataset = []
print_out = []
candidates = defaultdict(lambda: 0)
total_votes = 0

votes = namedtuple("votes","Voter_ID County Candidate")  # using namedtuple to keep list organized 

def analysis_dataset(data_set):
    for candidate in data_set:
        candidates[candidate.Candidate] += 1
    for votes in candidates.values():
        total_votes += votes
    print(total)

# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.

def main():
    with open(election_data, newline='') as csvfile: # reading CSV File and storing the rows into a list
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote = votes(row['Voter ID'], row['County'], row['Candidate'])  # appending monht of type months(namedTuple)
            dataset.append(vote)
    
    # The total number of votes cast
    print(len(dataset))
    # A complete list of candidates who received votes
    analysis_dataset(dataset)


main()