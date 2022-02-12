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
# Declare a variable for total votes at 0
total_votes = 0
# Declare a variable to hold unique candidate names.  Declare this variable as empty.
candidate_option = []
# Declare a empty dictionary to hold votes for each candidate.
candidate_votes = {}
# Declare candidate name and winning vote counter variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results csv file and read the file; this creates a variable.
with open(file_to_load) as election_data:
    # Read the file - this again creates a variable.
    file_reader = csv.reader(election_data)

    # Read and print out the header row.
    headers = next(file_reader)
    # print(headers) - commented out

    # Start a "for loop", create a variable "row" to iterate through each row in the for loop.
    for row in file_reader:
        # Count the total number of votes in the election - for every new row in the CSV file, increase "total_votes" by 1
        total_votes += 1

        # Get candidate name for each row in the for loop.
        candidate_name = row[2]

        # If the candidate_name is not in candidate_option, append the candidate names to the candidate option list using the append() method
        if candidate_name not in candidate_option:
            # Append the unique candidate names to the candidate_option list
            candidate_option.append(candidate_name)

            # Add the unique list of candidate names as keys to the dictionary candidate_vote, and set the value as 0 to each key.
            candidate_votes[candidate_name] = 0

        # In the for loop, add 1 to each occurrence of candidate_name
        candidate_votes[candidate_name] += 1

# Start populating results to the text file.
with open(file_to_save, "w") as txt_file:
    # Create a variable that hold the heading information
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")
    # Print the header information to terminal
    print(election_results)
    # Add heading information to the text file
    txt_file.write(election_results)

    # start a for loop to go through the candidate_vote dictionary, and get the vote count data for each candidate.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out the candidate name, the number of votes, and the percentage of the 
        print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})")
        # Write the output from each repetition to the text file
        txt_file.write(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

        if votes > winning_count and vote_percentage > winning_percentage:
            # If the above conditions are true, set the winning_count to the votes value, and winning_percentage to vote_percentage value
            winning_count = votes
            winning_percentage = vote_percentage
            # Again, if the conditions are met, set the winning_candidate to the current repetition candidate_name value (key in dict)
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.2f}%\n")
         # print(winning_candidate_summary) - commented out
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)