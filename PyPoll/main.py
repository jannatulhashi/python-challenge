#import os and csv modules

import os
import csv

# Get the current directory of main.py
current_dir = os.path.dirname(os.path.abspath("main.py"))

# Construct the file path to the election_data.csv file
csvpath = os.path.join(current_dir, "Resources", "election_data.csv")

# Define variables to hold the counts and percentages
total_votes = 0
candidates = []
candidate_votes = {}
candidate_percentages = {}

# Open the csv file and read in the data
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    header_row = next(csv_reader)
    # Loop over each row in the csv file
    for row in csv_reader:
        # Increment the total votes count
        total_votes += 1
        # Add candidate to list if not already present
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        # Increment the count of votes for the candidate
        candidate_votes[candidate] +=1

    # Calculate the percentage of votes each candidate won
    for candidate in candidate_votes:
        candidate_percentages[candidate] = round((candidate_votes[candidate] / total_votes) * 100, 3)

       
       

 # Determine the winner of the election based on popular vote
winner = max(candidate_votes, key = candidate_votes.get)

# In addition,final script should both print the analysis to the terminal and export a text file with the results.

# Print out the results to terminal
print("Election  Results")
print("--------------------------------------------------") 
print(f"Total Votes: {total_votes}")
print("--------------------------------------------------")

# Print out the results for each candidate
for candidate in candidates:
    if candidate in candidate_percentages and candidate in candidate_votes:
        percentage = round(candidate_percentages[candidate], 3)
        votes = candidate_votes[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")

print("--------------------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------------------")

# Export the analysis results to a text file
# Construct the file path to the Analysis text_file
analysis_path = os.path.join(current_dir, "Analysis", "election_results.txt")
with open(analysis_path, 'w') as text_file:
        text_file.write("Election Results\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("-------------------------\n")
        for candidate in candidates:
            if candidate in candidate_percentages and candidate in candidate_votes:
                percentage = round(candidate_percentages[candidate], 3)
                votes = candidate_votes[candidate]
                text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("-------------------------\n")

 

