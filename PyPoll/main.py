import os, csv
from collections import defaultdict,namedtuple

#reference to budget_data in ./Resources/budget_data.cs
election_data = os.path.join(os.getcwd(),'Resources/election_data.csv')
analysis = os.path.join(os.getcwd(),'Analysis/analysis.txt')
#Declaring variables to store the data from the CSV file
dataset = []
print_out = []
votes = namedtuple("votes","Voter_ID County Name")  # using namedtuple to keep list organized 

def analysis_dataset():
    candidates = defaultdict(lambda: 0)  # using defaultdict allows to count the votes for each candidate without having to worry about the initial value
    print_out.append("Election Results\n-------------------------")        
    for candidate in dataset:
        candidates[candidate.Name] += 1
    # sorting Dict out based on Votes 
    candidates = dict(sorted(candidates.items(),key=lambda i: i[1], reverse=True))
    # The total number of votes cast
    total_votes = len(dataset)
    print_out.append(f"Total Votes: {total_votes}\n-------------------------")
    for k,v in candidates.items():
        # The percentage of votes each candidate won
        percentage = "{0:.3f}%".format((v/total_votes)*100)
        print_out.append(f"{k}: {percentage} ({v})")
    # The winner of the election based on popular vote.
    winner = next(iter(candidates.keys())) # using nex(iter()) to get the first candidate in the dict, this because we previously sorted it out!!!
    print_out.append(f"-------------------------\nWinner: {winner}\n-------------------------")  
    # exports a text file with the results.
    with open(analysis, 'w+') as out_file:  # Generating analysis.txt printing out same result as in the console
        for line in print_out:
            print(line)
            out_file.write(line + '\n')

def main():
    with open(election_data, newline='') as csvfile: # reading CSV File and storing the rows into a list
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote = votes(row['Voter ID'], row['County'], row['Candidate'])  # appending canditate of type Candidates(namedTuple)
            dataset.append(vote)
    # A complete list of candidates who received votes
    analysis_dataset()

if __name__ == '__main__':
    main()