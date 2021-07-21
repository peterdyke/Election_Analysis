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
# Initialize a total vote counter
total_votes = 0
# Declare candidates list
candidate_options = []
# Declare empty dictionary to store candidate_name: total_votes
candidate_votes = {}

# Declare county list and county votes dictionary
county_options= []
county_votes= {}

# Declare Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county (highest count), county voter turnout (county count/ county largest *100)
county_largest= ""
county_count= 0
winning_county_percentage= 0

# Declare county list and dictionary 
# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read election data with csv reader function
    file_reader= csv.reader(election_data)
    # Read header row
    headers = next(file_reader)
    # For each rox in the election data CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get candidate name from each row
        candidate_name = row[2]
        # Get county name from each row
        county_name = row[1]

        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to list of candidates
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
         # add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

        # If county does not match existing county in the county list
        if county_name not in county_options:
            # Add county name to the county options list
            county_options.append(county_name)
            # And begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add a vote to the county's vote count
        county_votes[county_name] += 1

# Save Results to a text file        
with open (file_to_save, "w") as txt_file:
    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"--------------------------\n"
        f"\n")
    print (election_results, end = "")
    # Save final vote count as txt file
    txt_file.write (election_results)
    print ("County Votes: ")

    # Write a loop to get the county from the county dictionary
    for county_name in county_votes:
        # Retrieve county vote count
        votescounty = county_votes.get(county_name)
        # Calculate the percentage of votes for the county
        county_percentage = float(votescounty) / float (total_votes) * 100
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({votescounty:,})\n")
        # Print county results to terminal
        print (county_results, end = "")
        # Save county results to text file
        txt_file.write(county_results)
        # Determine winning county/ largest turnout
        if (votescounty > county_count) and (county_percentage > winning_county_percentage):
            county_largest= county_name

    county_largest_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: Denver\n"
        f"-------------------------\n")
    print (county_largest_summary)
    txt_file.write (county_largest_summary)

    for candidate_name in candidate_votes:
        # Retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidates voter count and percentages
        print (candidate_results, end= "")
        # Save candidate results to txt file
        txt_file.write (candidate_results)
        # Determine winning candidate and vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning count = votes, winning % to vote %
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate = candidate_name
            winning_candidate = candidate_name
        # Print winning candidate name, count, % to terminal
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print (winning_candidate_summary)
    # Save the winning candidate summary to txt file
    txt_file.write (winning_candidate_summary)