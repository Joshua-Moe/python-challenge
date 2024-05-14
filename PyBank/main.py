#!/usr/bin/env python3
import os

""" Module 3 Challenge

PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period


"""

def PyBank():

    summary_statement  = "Financial Analysis" + "\n\n" + "----------------------------\n\n"
    file = os.path.join("Resources","budget_data.csv")
    with open(file, 'r') as fh:
        date = []
        profit_losses = []
        lines = fh.readlines()
        header = lines[0] # I don't need the header for this; for the grading ruberic.
        for line in lines[1:]:
            date.append(line.strip().split(",")[0])
            profit_losses.append(float(line.strip().split(",")[1]))
        
        # The total number of months included in the dataset
        total_months = len(set(date))
        
        # The net total amount of "Profit/Losses" over the entire period
        net_total = sum(profit_losses)
        
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        delta_profit = []
        for i in range(len(profit_losses)-1):
            delta_profit.append(float(profit_losses[i+1]-profit_losses[i]))
            
        averageChanges = round(sum(delta_profit)/len(delta_profit), 2)
        
        
        #The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in profits (date and amount) over the entire period
        
        for i in range(len(delta_profit)):
            if delta_profit[i] == max(delta_profit):
                greatestIncrease_date = date[i+1]
            elif delta_profit[i] == min(delta_profit):
                greatestDecrease_date = date[i+1]
            else:
                continue
        
        
        summary_statement += f"Total Months: {total_months}\n\n"
        summary_statement += f"Total: ${net_total}\n\n"
        summary_statement += f"Average Change: ${averageChanges}\n\n"
        summary_statement += f"Greatest Increase in Profits: {greatestIncrease_date} (${max(delta_profit)})\n\n"
        summary_statement += f"Greatest Decrease in Profits: {greatestDecrease_date} (${min(delta_profit)})\n"
        print(summary_statement)
            
    # Saving to output file
    output_path = os.path.join("analysis","PyBank_output.txt")
    with open(output_path,'w') as fh:
        fh.write(summary_statement)
        
if __name__=="__main__":
    PyBank()
