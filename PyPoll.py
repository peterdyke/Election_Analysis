#The data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate received
# 5. The winner of the election based on popular vote
# path to data file = resources/election_results.csv
# with open(file_to_save, "w") as txt_file:
    # write three counties to the file
    #txt_file.write("whatever you want to write")

# Add dependencies
import os
import csv
# assign variable for indirect path to election data
file_to_load = os.path.join ("Resources", "election_results.csv")
# Create a filename variable to write a path to the file 
file_to_save= os.path.join('analysis', 'election_results.txt')
# 1. Initialize a total vote counter
total_votes = 0
# Declare Candidates list
candidate_options = []
# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read election data with csv reader function
    file_reader= csv.reader(election_data)
    # Read header row
    headers = next(file_reader)
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        # Print candidate name from each row
        candidate_name = row[2]
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to list of candidates
            candidate_options.append(candidate_name)

    # Print the candidate list
    print (candidate_options)



