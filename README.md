# Election_Analysis

## Project Overview
We were tasked by the an employee of the Colorado Board of Elections to audit a local congressional election. They asked us to do the following:
1. Calculate the total number of votes cast.
2. Determine the number of votes and percentage of votes cast for each county in the election.
3. Determine the county with the largest number of votes cast.
4. Determine the number of votes and percentage of votes cast that each candidate received.
5. Determine the winner of the election through popular vote and show both how many votes and the percentage of votes that the winning candidate received.

## Resources
Data Source: election_results.csv

Software used: Python 3.8.8, Virtual Studio Code Version: 1.57.0

## Summary
Using Python we were able to write a script that will allow the Election Commission to use this script in future elections to determine the number of votes cast overall, in each county, and for each candidate. Results are below.

## Challenge Results
Our results are described in the image below, with a description of the process in the following bullet points.
<img src=Resources/election_analysis.png>

1. To determine the total votes counted we first initialized a total vote counter by assigning the variable 'total_votes = 0'.
    * We then read through the provided csv file with the election data, adding 1 to the total_vote variable with each row of the data set.  

        for row in file_reader:

        total_votes += 1
2. In a similar fashion, we determined the number of votes each county received by first creating an empty county options list, county_options = [], and an empty county votes dictionary, county_votes = {}.  

    *   if county_name not in county_options:

            county_options.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] += 1
    * We then found the percentage of votes cast for each county by dividing the votes cast in each county by the total votes cast in the election, and muliplying by 100.

        county_percentage = float(votescounty) / float (total_votes) * 100
3. For the largest county, or the county that received the most votes, we used a simple if statement to see if the vote county for each county (variable = votescounty) was greater than the previous county.
    * if (votescounty > county_count):

            county_count = votescounty
        
            county_largest= county_name

4. We used the same process to determine the candidate that received the most votes and that candidate's percentage of the vote.
    * if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
    * for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100
5. Then using and if statement, we checked to see if the number of votes each candidate received was greater than the previous candidate, and if the percentage of the vote they received was larger than the previous candidate. If both conditions were true, that candidate was our winner.

    * if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate_name


## Challenge Summary
So as you can see with our election results and process, we were able to determine all relevant data from this election through a simple script. As long as the data provided is in the same format, this same script could be used for any election with minimal modification, to determine the results of that election. For instance, if multiple candidates were in a given county we could determine the number of votes and percentages of votes received by each candidate both within the county and across the larger election. If given multiple years of election data we could also track how well candidates did across time and see which candidates gained or lost in popularity as time progressed. This could be interesting to see an upstart candidate gain in the pecentage of the vote over time to overtake an incumbent and win an election.
