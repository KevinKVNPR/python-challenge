import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))
election_data_cvs= os.path.join("Resources", "election_data.csv")

with open(election_data_cvs, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
file = open(election_data_cvs)
reader = csv.reader(file)
header = next(reader)

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
VOTERID_COL = 0
COUNTY_COL = 1
CANDIDATE_COL = 2

for row in reader:
    total_votes = total_votes + 1

candidate_name = row[CANDIDATE_COL]

if candidate_name not in candidate_options:

    candidate_options.append(candidate_name)

    candidate_votes[candidate_name] = 0

candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) / float(total_votes) * 100
    
    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate

#Print out Data: 
output =(
f"\nElection Results\n"
f"-------------------\n"
f"Total Votes {total_votes}\n"
f"-------------------\n"
f"{candidate_options}: {vote_percentage}% ({votes})\n"
f"\n-------------------\n"
f"Winner: {winning_candidate}"
"\n-------------------\n"
)
print(output)

file_output = os.path.join("Election_Results.txt")
with open(file_output, "w") as textfile:
    textfile.write(output)