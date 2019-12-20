import os
import csv

budget_data_csv = os.path.join('PyBank_Work', 'Budget_Data.csv')

month = 0
months = {}
total = 0
profit = 0
sum_profit = 0
sum_loss = 0
profitlosstotal = 0

print('Financial Analysis')
print('--------------------------')

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

        month = row[0]
        total = total + 1
        
    if month in months:
            months[month] = months[month] + 1
    else:
        months[month] = 1

    for row in csvreader:
        profit = int(row[1])
    if profit > 0:
        sum_profit = sum_loss + profit
    elif profit < 0:
        sum_loss = sum_loss + profit
    profitlosstotal = sum_profit - sum_loss
   


print('Total Months' + ':' + str(total - 1))
print(f"Profit/Loss : {profitlosstotal}")

