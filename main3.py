import csv
import os

budget_data = "budget_data.csv"
months = []
profitloss = []
profitchange = []
change_list = []

with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")   
   next(csvreader)   
   for row in csvreader:
       months.append(row[0])
       profitloss.append(float(row[1]))   
   for i in range(1, len(profitloss)):
       profitchange.append(profitloss[i]-profitloss[i-1])       
       changes = round(sum(profitchange)/len(profitchange), 2)       
       max_change = max(profitchange)
       max_date = str(months[profitchange.index(max(profitchange))+ 1])
       min_change = min(profitchange)
       min_date = str(months[profitchange.index(min(profitchange))+ 1])
       
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${int(sum(profitloss))}")
print(f"Average Change: ${(changes)}")
print(f"Greatest increase in profits: {max_date} ${int(max_change)}")
print(f"Greatest decrease in profits: {min_date} ${int(min_change)}")

fh = open("pybank.txt", "w")
fh.write("Financial Analysis\n"
"-------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${int(sum(profitloss))}\n"
f"Average Change: ${(changes)}\n"
f"Greatest increase in profits: {max_date} ${int(max_change)})\n"
f"Greatest decrease in profits: {min_date} ${int(min_change)})")
fh.close()
