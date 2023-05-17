# Step 1: Import libraries and dependencies
import os
import csv

# Get the current directory of main.py
current_dir = os.path.dirname(os.path.abspath("main.py"))

# Construct the file path to the budget_data.csv file
csvpath = os.path.join(current_dir, "Resources", "budget_data.csv")

# Step 2: Read the budget_data.csv file
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    # skip header row
    header_row = next(csv_reader)  
    financial_data = list(csv_reader)

# Step 3: Initialize variables
total_months = 0
net_total = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 0]
previous_month_profit = 0
changes = []

# Step 4: Loop through the financial data and perform calculations
for record in financial_data:
    # Increment total months
    total_months += 1
    
    # Add "Profit/Losses" value to net total
    net_total += int(record[1])
    
    # Calculate change in "Profit/Losses" and add to changes list
    current_month_profit = int(record[1])
    if total_months > 1:
        change = current_month_profit - previous_month_profit
        changes.append(change)
    
        # Update greatest increase and decrease in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = record[0]
            greatest_increase[1] = change
        elif change < greatest_decrease[1]:
            greatest_decrease[0] = record[0]
            greatest_decrease[1] = change
    
    # Set current month's profit as previous month's profit for next iteration
    previous_month_profit = current_month_profit

# Step 5: Calculate average change in "Profit/Losses"
average_change = sum(changes) / len(changes)
# Step 6: Print results to the terminal
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in  Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the analysis results to a text file
# Construct the file path to the Analysis text_file
analysis_path = os.path.join("current_dir", "Analysis", "financial_analysis.txt")
with open("analysis_path", 'w') as text_file:
 text_file.write("Financial Analysis\n")
 text_file.write("-----------------------------\n")
 text_file.write(f"Total Months: {total_months}\n")
 text_file.write(f"Total: ${net_total}\n")
 text_file.write(f"Average Change: ${round(average_change, 2)}\n")
 text_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
 text_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


            
        
        
        
        
        
    

   

