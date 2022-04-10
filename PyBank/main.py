import os
import csv

csvpath = os.path.join('budget_data.csv')

total_profit_losses = 0
total_change = 0
months = 0
current = 0
last = 0
change = []
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 99999999999
greatest_dec_month = ""

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
         
    for row in csvreader:
        
                  
        # calculating the net total amount of "Profit/Losses" over the entire period
        total_profit_losses = total_profit_losses + int(row[1])

        # changes in "Profit/Losses" over the entire period, and then the average of those changes
        current = int(row[1])
        months = months + 1

        if months > 1:
            change.append(current - last)     
        last = int(row[1])

        #calculating the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

        #calculating the greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0] 
        
# calculating average change 
total_change = sum(change)
average_change = round(total_change / (months - 1), 2)
         
print("\nFinancial Analysis \n----------------------------")
print("Total Months: " + str(months))
print("Total: " + "$" + str(total_profit_losses))
print("Average Change: " + "$" + str(average_change))
# Need Help with this --> not returning the right month
print(f"Greatest Increase in Profits: {greatest_inc_month} (${str(max(change))})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${str(min(change))})")


with open("financial_anylysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis \n----------------------------")
    txt_file.write('\n' + "Total Months: " + str(months))
    txt_file.write('\n' + "Total: " + "$" + str(total_profit_losses)) 
    txt_file.write('\n' + "Average Change: " + "$" + str(average_change))
    txt_file.write(f'\n' + "Greatest Increase in Profits: " + {greatest_inc_month} + "$" ({(max(change))}))
    txt_file.write(f'\n' + "Greatest Decrease in Profits: " + {greatest_dec_month} + "$" ({(min(change))}))

