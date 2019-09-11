#import Path and csv
from pathlib import Path
import csv

#set data file path

csvpath = Path("Resources/budget_data.csv")

#initialize variables to count months, sum profits and losses, sum of Pnl changes,
#maximum PnL change and date, minimum PnL change and date

count_months = 0
sum_pnl = 0
sum_pnl_delta = 0
max_pnl_delta = 0
max_pnl_date = ""
min_pnl_delta = 0
min_pnl_date = ""


#open data file in read mode

with open(csvpath,"r") as datafile:
    csvreader = csv.reader(datafile, delimiter = ',')
    header = next(csvreader)
    
    #pass first row as first data point
    first_row = next(csvreader)
    first_pnl = int(first_row[1])
    count_months = 1
    sum_pnl = first_pnl
    
    #assign first PnL as initial reference for Pnl change loop below
    prev_pnl = first_pnl
    
    #loop through rest of data
    for row in csvreader:
        curr_date = row[0]
        curr_pnl = int(row[1])
        
        #continue counting and calculating cummulative PnL
        count_months += 1
        sum_pnl += curr_pnl
        
        #calculate PnL change, and cummulative Pnl change sum
        pnl_delta = curr_pnl - prev_pnl
        sum_pnl_delta += pnl_delta
        
        #determine max and min PnL change and date
        if pnl_delta > max_pnl_delta:
            max_pnl_delta = pnl_delta
            max_pnl_date = curr_date
        elif pnl_delta < min_pnl_delta:
            min_pnl_delta = pnl_delta
            min_pnl_date = curr_date
        
        #assign current PnL as previous PnL for next loop
        prev_pnl = curr_pnl

#calculate average PnL change
average_pnl_delta = round(sum_pnl_delta / (count_months - 1),2)

#what to print
text_to_print = f"Financial Analysis\n------------------\nTotal Months: {count_months}\nTotal: ${sum_pnl}\nAverage  Change: ${average_pnl_delta}\nGreatest Increase in Profits: {max_pnl_date} (${max_pnl_delta})\nGreatest Decrease in Profits: {min_pnl_date} (${min_pnl_delta})"

#print on terminal
print(text_to_print)

#export to text file
outputpath = Path("output.txt")

with open(outputpath,'w') as output:
    output.write(text_to_print)