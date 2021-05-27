# Results Needed:
# Total Number of Votes
# List of Canidates
# Percentage of Votes per Candidte
# Total Number of Votes per Candidate
# Winner of Election based on Popular Vote

import csv
import os

#Assign a variable to the file path
election_file = os.path.join("resources", "election_results.csv")
write_election_file = os.path.join("analysis", "election_analysis.txt")

#Assign a variable to open the file
with open(election_file) as election_data:

    #To Do
    #print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
        #print(row)

    #Write data
    #with open(write_election_file,"w") as outfile:
        #outfile.write("Arapahoe\nDenver\nJefferson")

