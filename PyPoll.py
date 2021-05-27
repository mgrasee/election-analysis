# Needed Results
# Total Number of Votes
# List of Canidates
# Percentage of Votes per Candidte
# Total Number of Votes per Candidate
# Winner of Election based on Popular Vote

#Dependencies
import csv
import os

#Assign a variable to the read file path
election_file = os.path.join("resources", "election_results.csv")

#Assign a variable to the write file path
write_election_file = os.path.join("analysis", "election_analysis.txt")

# Variable to count total votes
total_votes = 0

#Candidates
candidate_options = []

#Candidates Votes
candidate_votes = {}

#Determine Winner

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Assign a variable to open the file
with open(election_file) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read Headers
    headers = next(file_reader)

    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n")
print(winning_candidate_summary)
#print(total_votes)
#print(candidate_votes)

    #Write data
    #with open(write_election_file,"w") as outfile:
        #outfile.write("Arapahoe\nDenver\nJefferson")

