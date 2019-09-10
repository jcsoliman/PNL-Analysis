#budget_data.csv 
#csv file is a dictionary mmm-yyyy,float

from pathlib import Path
import csv

csvpath = Path("../../CU-NYC-FIN-PT-08-2019-U-C/02-Homework/02-Python/Pybank/Resources/budget_data.csv")

##The total number of months included in the dataset.

#--count of periods: return sum of count mmm-yyyy
#--import then count?
#--loop through each keym, then sum +=?

#https://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list


##The net total amount of Profit/Losses over the entire period.

#--return sum of values
#--loop through each value, then sum +=?
#--is there a more efficient code?


##The average of the changes in Profit/Losses over the entire period.

#--create variable that calculate delta PNL every period
#--add these delta to dictionary? nest dictionary? convert to nested dict {mmm-yyyy:[PnL:value,Delta:value]}??? 
#--loop through each delta, then sum +=?
#--sum / count of periods - 1


#The greatest increase in profits (date and amount) over the entire period.

#get max of delta
#do we want to loop through and do a compare if prev > current?
#do we want to create a list, get max of list, pull value of that delta? --
#return string with month, PnL


#The greatest decrease in losses (date and amount) over the entire period.

#get min of delta
#do we want to loop through and do a compare if prev > current?
#do we want to create a list, get min of list, pull value of that delta? --
#return string with month, PnL

##Your final script should print the analysis to the terminal and export a text file with the results.