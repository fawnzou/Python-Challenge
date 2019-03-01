
import os
import csv

# Open and read csv
budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")
with open(budget_data_csv_path, newline="", encoding='utf-8-sig') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    total_months = 0
    prev_amount=0
    cur_amount=0
    change_amount=0
    # set a dictionary to hold profit change as key, date as value
    change_amount_dic = {}
    greatest_increase = 0
    greatest_decrease = 0
    ave_change=0
   
    # Read through each row of data 
    for row in csv_reader:
        #Month count
        total_months+=1
        if total_months ==2:
            # Set the value of 'Profit/Losses' in the first row as previous amount
            # convert value of 'Profit/Losses' from string to float
            prev_amount=float(row[1])
            # add value to total_amount
            total_amount+=float(row[1])
        elif total_months >2:
            # add value to total_amount
            total_amount+=float(row[1])
            # Keep track change amount, and put it into dictionary as key,put its date into
            # dictionary as key
            cur_amount=float(row[1])
            change_amount=cur_amount-prev_amount
            change_amount_dic[change_amount]=row[0]
            prev_amount=cur_amount

greatest_increase = max(change_amount_dic)
greatest_increase_month=change_amount_dic[greatest_increase]
greatest_increase=int(greatest_increase)
greatest_decrease = min(change_amount_dic)
greatest_decrease_month=change_amount_dic[greatest_decrease]
greatest_decrease=int(greatest_decrease)
ave_change = round((sum(change_amount_dic)/len(change_amount_dic)),2)

#Output result
print ("Financial Analysis") 
print ('-'*30)
print (f'Total Months: {total_months-1}')
print (f'Total: ${int(total_amount)}')
print(f'Average Change: ${ave_change}')
print (f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print (f'Greatest decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
       


