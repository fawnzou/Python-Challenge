import os
import csv
budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")
with open(budget_data_csv_path, newline="", encoding='utf-8-sig') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    total_months = 0
    total_amount = 0
    pre_amount=0
    cur_amount=0
    change_amount=0
    
    change_amount_dic = {}
    greatest_increase = 0
    greatest_decrease = 0
    ave_change=0
   
    for row in csv_reader:
        total_months+=1
        if total_months ==2:
            pre_amount=float(row[1])
            cur_amount=float(row[1])
            total_amount=float(row[1])
        elif total_months >2:
            total_amount+=float(row[1])
            pre_amount=cur_amount
            cur_amount=float(row[1])
            change_amount=cur_amount-pre_amount
            change_amount_dic[change_amount]=row[0]
            
greatest_increase = max(change_amount_dic)
greatest_increase_month=change_amount_dic[greatest_increase]
greatest_increase=int(greatest_increase)
greatest_decrease = min(change_amount_dic)
greatest_decrease_month=change_amount_dic[greatest_decrease]
greatest_decrease=int(greatest_decrease)
ave_change = round(sum(change_amount_dic)/len(change_amount_dic),2)

print ("Financial Analysis") 
print ('-'*30)
print (f'Total Months: {total_months-1}')
print (f'Total: ${int(total_amount)}')
print (f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print (f'Greatest decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
