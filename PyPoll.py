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

# Add out dependencies
import os
import csv
# assign variable for indirect path to election data
file_to_load = os.path.join ("Resources", "election_results.csv")
# Create a filename variable to write a path to the file 
file_to_save= os.path.join('analysis', 'election_results.txt')
# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read election data with csv reader function
    file_reader= csv.reader(election_data)
    #print header row
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        print(row)
