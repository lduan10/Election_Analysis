# The data we need to retrive:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the csv and os dependencies for use.
import csv
import os

# Assign a filename variable to point to the file to open.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a filename variable to point to the file to save (create a txt file).
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results csv file and read the file; this creates a variable.
with open(file_to_load) as election_data:
    # Read the file - this again creates a variable.
    file_reader = csv.reader(election_data)

    # Read and print out the header row.
    headers = next(file_reader)
    print(headers)