import os, csv
from collections import defaultdict

election_data = os.path.join(os.getcwd(),'Resources/election_data.csv') #reference to election_data in ./Resources/election_data.csv.cs
analysis = os.path.join(os.getcwd(),'Analysis/analysis.txt')  # output path.
#Declaring variables to store the data from the CSV file
print_out = []
candidates = defaultdict(lambda: 0)  # using defaultdict allows to count the votes for each candidate without having to worry about the initial value

def analysis_dataset(candidates):
    print_out.append("Election Results\n-------------------------")        
    # sorting Dict out based on Votes 
    candidates = dict(sorted(candidates.items(),key=lambda i: i[1], reverse=True))
    # The total number of votes cast
    total_votes = sum([votes for votes in candidates.values()]) # where Values() represent total votes received for each candidate
    print_out.append(f"Total Votes: {total_votes}\n-------------------------")
    for k,v in candidates.items(): # where k=Candidate's name and v=total votes
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
            candidates[row['Candidate']] += 1 # getting a complete list of candidates who received votes
    analysis_dataset(candidates)

if __name__ == '__main__':
    main()
