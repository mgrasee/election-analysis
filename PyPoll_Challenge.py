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

#Candidates/County
candidate_options = []
county_options = []

#Candidates/County Votes
candidate_votes = {}
county_votes = {}

#Determine Winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0
highest_county = ""
highest_county_count = 0
highest_county_percentage = 0

#Assign a variable to open the file
with open(election_file) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read Headers
    headers = next(file_reader)

    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] +=1
with open(write_election_file,"w") as outfile:
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    outfile.write(election_results)
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        cvote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)
        outfile.write(county_results)
        if(cvotes > highest_county_count) and (cvote_percentage > highest_county_percentage):
            highest_county_count = cvotes
            highest_county_percentage = cvote_percentage
            highest_county = county_name
    winning_county_summary = (
        f"--------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"--------------------\n")
    print(winning_county_summary)
    outfile.write(winning_county_summary)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        canidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(canidate_results)
        outfile.write(canidate_results)
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
    outfile.write(winning_candidate_summary)