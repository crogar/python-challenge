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
    votes= []
    for candidate in data_set:
        candidates[candidate.Candidate] += 1
    candidates = dict(sorted(candidates.items(),key=lambda i: i[1], reverse=True))
    # The total number of votes cast
    total_votes = len(data_set)
    for k,v in candidates.items():
        percentage = "{0:.3f}%".format((v/total_votes)*100)
        votes.append(f"{k} {percentage} ({v})")
    print(votes)
# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.

def main():
    with open(election_data, newline='') as csvfile: # reading CSV File and storing the rows into a list
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote = votes(row['Voter ID'], row['County'], row['Candidate'])  # appending canditate of type Candidates(namedTuple)
            dataset.append(vote)
    
   
    print(len(dataset))
    # A complete list of candidates who received votes
    analysis_dataset(dataset)


main()