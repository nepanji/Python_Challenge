# Import Dependencies
# Import CSV cmdlet to create custom objects from the items in the CSV file to make parsing info easier.
import csv

# Open the file
with open('Resources/election_data.csv', 'r') as csvfile:
    election_data = csv.reader(csvfile)

    # Determine variables need to complete code
    vote_tally = 0
    voters = 0
    winner_tally = 0
    poll_results = {}
    ballot_names = []
    percent_vote = {}
    
    
    # Skip the first row
    next(election_data)
    
    # Read through the csv file and start votes counter to get total votes
    for row in election_data:
        vote_tally += 1

        # Create list for candidate names and their votes from election day
        if row[2] not in ballot_names:
            ballot_names.append(row[2])
            poll_results[row[2]] = 1
        else:
            poll_results[row[2]] += 1
            
  
for candidate_name, votes in poll_results.items():
    percent_vote[candidate_name] = round((votes/vote_tally)*100, 2)
    if votes > winner_tally:
        winner_tally = votes
        winner = candidate_name



election_results = f"""
Election Results
-------------------------
Total Votes: {vote_tally}
-------------------------
Khan: {percent_vote['Khan']}% ({poll_results['Khan']})
Correy: {percent_vote['Correy']}% ({poll_results['Correy']})
Li: {percent_vote['Li']}% ({poll_results['Li']})
O'Tooley: {percent_vote["O'Tooley"]}% ({poll_results["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------
"""

print(election_results)

with open('Analysis/election_results.txt', 'w') as txtfile:
    txtfile.write(election_results)