import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..','pyPoll', 'Resources', 'election_data.csv')


# Read in the CSV file
with open(election_data, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader, None)

    # prepare lists & variables
    candidates = []
    votes = []
    can_can = []
    can_perc = []
    can_votes = []
    total_votes = 0
    vote_count = 0
    percentage = 0

    # Loop through the data to get list of all candidates & votes
    for row in csvreader:
        votes.append(total_votes)
        candidates.append(row[2])
        total_votes += 1
    
    #create set to get unique candidates, revert to list to allow iteration
    candid_set = set(candidates)
    can_can = list(candid_set)

    #find vote count and percentage for each candidate
    for candid in can_can:
        #reset vote count for each candidate    
        vote_count = 0

        #tabulate number of votes for candidate
        for vote in votes:
            if candidates[vote] == candid:
                vote_count += 1
            
        #calculate & format percentage
        percentage = '{0:.00%}'.format(vote_count / total_votes) #* 100
        
        #add candidate percent and votes to lists
        can_perc.append(percentage)
        can_votes.append(vote_count)

#determine winner
winner = can_can[can_votes.index(max(can_votes))]
        
#print results
print('Election Results')
print('------------------------------')
print(f'Total Votes: {vote_count}')
print('------------------------------')
for c in can_can:
    print(f'{c}: {can_perc[can_can.index(c)]} ({can_votes[can_can.index(c)]})')
print('------------------------------')
print(f'Winner: {winner}')
print('------------------------------')

#output analysis to file
output_path = os.path.join('..','pyPoll', 'Resources', 'analysis.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Total Votes:', vote_count])
    csvwriter.writerow(['------------------------------'])
    for c in can_can:
        csvwriter.writerow([c,':', can_perc[can_can.index(c)], '(',can_votes[can_can.index(c)],')'])
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Winner:', winner])
    csvwriter.writerow(['------------------------------'])