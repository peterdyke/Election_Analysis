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
# Declare Winning Candidate adn Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read election data with csv reader function
    file_reader= csv.reader(election_data)
    # Read header row
    headers = next(file_reader)
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print candidate name from each row
        candidate_name = row[2]
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to list of candidates
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
         # add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1
with open (file_to_save, "w") as txt_file:
    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total VotesL {total_votes:,}\n"
        f"--------------------------\n")
    print (election_results, end = "")
    # Save final vote count as txt file
    txt_file.write (election_results)
    for candidate_name in candidate_votes:
        # Retreive vote count for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidates voter count and percentages
        print (candidate_results)
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