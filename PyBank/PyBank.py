import os
import csv
import sys

filepath = os.path.join("..","Resources", "budget_data.csv")

with open('budget_data.csv') as file:
    
    csvReader = csv.DictReader(file, delimiter=",")
    line_count = 0
    print(csvReader)

    TotalMonths = 0
    NetTotal = 0
    AvgChange = 0
    GreatestIncrease = 0
    GreatestIncreaseDate = 0
    GreatestDecrease = 0
    GreatestDecreaseDate = 0
    PreviousAmount = 0
    changesum = 0
    line_count2 = 0
                                        
    for row in csvReader:                       # We use a for loop to iterate through the file one line at a time.
        
        TotalMonths += 1
        NetTotal = NetTotal + int(row["Profit/Losses"])
        

        if line_count2 == 0 :
            #changesum = int(row["Profit/Losses"])
            PreviousAmount = int(row["Profit/Losses"])
        currentAmount = int(row["Profit/Losses"])
        change = currentAmount - PreviousAmount
        changesum += change
        PreviousAmount = int(row["Profit/Losses"])

        
        if GreatestIncrease < change :
            GreatestIncrease = change
            GreatestIncreaseDate = row["Date"]

        if GreatestDecrease > change :
            GreatestDecrease = change
            GreatestDecreaseDate = row["Date"]
        line_count2 += 1        
AvgChange = round(changesum / TotalMonths,2)     

print("Total Months: ", TotalMonths)
print("Total: $", NetTotal)
print("Average Change: $", AvgChange)
print("Greatest Increase in Profits:  ",GreatestIncreaseDate, ' ($', GreatestIncrease,')' )
print("Greatest Decrease in Profits:  ",GreatestDecreaseDate, ' ($', GreatestDecrease,')' )

#Write to .txt document
with open("PyBank.txt", mode = "w") as f:
    f.write("Total Months: "+ str(TotalMonths))
    f.write("\n" "Total: $"+ str( NetTotal))
    f.write("\n" "Average Change: $"+ str( AvgChange))
    f.write("\n" "Greatest Increase in Profits:  "+ str(GreatestIncreaseDate) +' ($'+ str(GreatestIncrease) +')' )
    f.write("\n" "Greatest Decrease in Profits:  "+ str(GreatestDecreaseDate) +' ($'+ str(GreatestDecrease) +')' )
