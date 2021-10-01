# Import CSV cmdlet to create custom objects from the items in the CSV file to make parsing info easier.
import csv
# Import os cmdlet to navigate the file system to look up anc change file variables 
import os

# Create an os independent file path to read the csv file
csvpath = os.path.join('Resources','budget_data.csv')

# Open the file
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    # Read the header row
    next(csvreader)

    # Create empty lists for budget data
    months = []
    new_month = []
    profit_loss = []
    pl_change = []
    pl_change_list = []
    previous = 0
    change_diff = 0

    # Read through the csv file
    for x in csvreader:
        
        months.append(x[0])
        profit_loss.append(int(x[1]))

        # Calculate difference in P/l line by line
        change_diff = int(x[1]) - int(previous)
        change_diff_month = x[0]
        previous = int(x[1])
        
        
        # Add change to p/l change list
        pl_change.append(int(change_diff))
        new_month.append(change_diff_month)
    
    #Remove initial profit loss value from new list
    first_pl = pl_change.pop(0)
    
    
    # Define variables for equations to calculate length of months and sum of profit loss
    total_mos = len(months)
    total_profit_loss = sum(profit_loss)
    avg_change =sum(pl_change)/len(pl_change)
    max_increase_pl = max(pl_change)
    min_increase_pl = min(pl_change)
    
     
    # Find location of max increase and min increase
    max_increase_dt = pl_change.index(max(pl_change)) + 1
    min_increase_dt = pl_change.index(min(pl_change)) + 1
    # print(max_increase_dt)
    # print(min_increase_dt)

    # Make Finanacial Analysis chart
    print(f" ")
    print(f"Financial Analysis")
    print(f"--------------------------------------------")
    print(f"Total Months: {total_mos}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {new_month[int(max_increase_dt)]} (${max_increase_pl})")
    print(f"Greatest Decrease in Profits: {new_month[int(min_increase_dt)]} (${min_increase_pl})")
    print(f" ")
  

   
    # Create a text file 
    output = os.path.join('bank_data.txt')

    with open(output, "w") as textfile:
        textfile.write(
            print(f"Financial Analysis")
            print(f"--------------------------------------------")
            print(f"Total Months: {total_mos}")
            print(f"Total: ${total_profit_loss}")
            print(f"Average Change: ${avg_change}")
            print(f"Greatest Increase in Profits: {new_month[int(max_increase_dt)]} (${max_increase_pl})")
            print(f"Greatest Decrease in Profits: {new_month[int(min_increase_dt)]} (${min_increase_pl})")
        )  


       

        