
import os
import csv

inputFilePath = os.path.join('..','03-Python_Python Homework_Instructions_PyBank_Resources_budget_data.csv')

    
month_count = 0
netTotalPL = 0
change = []
oldPL = 0
maxIncrease = 0
maxDecrease = 0

with open(inputFilePath,newline = '') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")
    csvHeader = next(csvReader)
    for row in csvReader:
        month_count+=1
        netTotalPL += float((row[1]))
        if month_count==1:
            oldPL = float(row[1])
        else:
            currentChange = float(row[1])-oldPL
            change.append(currentChange)
            oldPL = float(row[1])
            if currentChange > 0  and currentChange > maxIncrease:
                maxIncrease = currentChange
                maxIncreaseDate = row[0]
            if currentChange < 0 and currentChange <maxDecrease:
                maxDecrease = currentChange
                maxDecreaseDate = row[0]
    
                
    print(f"The net Total is: ${netTotalPL}")        
    print(f'The total number of months is: {month_count}')
    print(f"The average change is: ${sum(change)/len(change)}")
    print(f'The greatest increase in profits is: ${maxIncrease} on {maxIncreaseDate}')
    print(f'The greatest decrease in profits is: ${maxDecrease} on {maxDecreaseDate}')
    
outputFileName = 'pyBankSummary.txt'
outputFilePath = os.path.join(outputFileName)
with open(outputFilePath,'w') as outFile:
    outFile.write(f"The net Total is: ${netTotalPL}\n")        
    outFile.write(f'The total number of months is: {month_count}\n')
    outFile.write(f"The average change is: ${sum(change)/len(change)}\n")
    outFile.write(f'The greatest increase in profits is: ${maxIncrease} on {maxIncreaseDate}\n')
    outFile.write(f'The greatest decrease in profits is: ${maxDecrease} on {maxDecreaseDate}\n')
    

            

        
        
       
        
        
