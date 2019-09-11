import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('..','pyBank', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(budget_data, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader, None)

    # prepare lists
    all_months = []
    PandL_val = []
    change_val = []

    # Loop through the data
    for row in csvreader:
        
        #insert csv values into lists
        all_months.append(row[0])
        PandL_val.append(int(row[1]))

        #generate list of changes from month to month
        if len(PandL_val) >= 2:
          change_val.append((PandL_val[len(PandL_val)-1] - PandL_val[len(PandL_val)-2]))
        
    #calculate & format totals
    total_months = len(all_months)
    total_PandL = '${:,}'.format(sum(PandL_val))

    #calculate & format average change
    avg_change = sum(change_val) / total_months
    avg_change = '${:,.2f}'.format(avg_change)
    
    #find & format max values from list
    max_month = PandL_val.index(max(PandL_val))
    max_month = all_months[max_month]
    max_val = '${:,}'.format(max(PandL_val))

    #find & format min values from list
    min_month = PandL_val.index(min(PandL_val))
    min_month = all_months[min_month]
    min_val = '${:,}'.format(min(PandL_val))

#print analysis
print('Financial Analysis')
print('------------------------------')
print(f'Total Months:', total_months)
print(f'Total:', total_PandL)
print(f'Average Change:', avg_change)
print(f'Greatest Increase in Profits:', max_month, max_val)
print(f'Greatest Decrease in Profits:', min_month, min_val)

#output analysis to file
output_path = os.path.join('..','pyBank', 'Resources', 'analysis.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write rows
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Total Months', total_months])
    csvwriter.writerow(['Total:', total_PandL])
    csvwriter.writerow(['Average Change', avg_change])
    csvwriter.writerow(['Greatest Increase in Profits', max_month, max_val])
    csvwriter.writerow(['Greatest Decrease in Profits', min_month, min_val])
