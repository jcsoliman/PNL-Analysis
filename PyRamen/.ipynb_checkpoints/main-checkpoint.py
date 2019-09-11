#import path and csv
from pathlib import Path
import csv

#read menu data
menudatafile = Path("Resources/menu_data.csv")
menulist = []

with open(menudatafile,'r') as menu:
    menureader = csv.reader(menu,delimiter=',')
    menuheader = next(menureader)
    
    for menuitem in menureader:
        menulist.append(menuitem)

#read sales data
salesdatafile = Path("Resources/sales_data.csv")
saleslist = []

with open(salesdatafile,'r') as sales:
    salesreader = csv.reader(sales,delimiter=',')
    salesheader = next(salesreader)
    
    for salesitem in salesreader:
        saleslist.append(salesitem)

#initialize report dictionary
report = {}

#loop through each sales record 
for salesitem in saleslist:
    
    #assign variables to qty and product
    quantity = int(salesitem[3])
    product = salesitem[4]
    
    #add product if not in dictionary
    if product not in report.keys():
        report[product] = {"01-count": 0,"02-revenue": 0,"03-cogs": 0,"04-profit": 0}
    
    #loop through each menu item
    for menuitem in menulist:
        
        #assign variables to item, price and cost
        item = menuitem[0]
        price = float(menuitem[3])
        cost = float(menuitem[4])
        
        #capture qty, revenue, cogs, profit for matching sales and menu item
        if product == item:
            profit = quantity * (price - cost)
            report[product]["01-count"] += quantity
            report[product]["02-revenue"] += price * quantity
            report[product]["03-cogs"] += cost * quantity
            report[product]["04-profit"] += profit
        #else: print(f"{product} does not equal {item}! NO MATCH!")

#compose report text
text_to_write = ""

for key,value in report.items():
    text_to_write += f"{key} {value} \n"

#define report file
reportpath = Path("report.txt")

#write report text to report file
with open(reportpath,'w') as reportfile:
    reportfile.write(text_to_write)