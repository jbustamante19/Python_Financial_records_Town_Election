import os
import csv

fileName = '03-Python_Python Homework_Instructions_PyPoll_Resources_election_data.csv'
inputFilePath = os.path.join('..',fileName)

totalVotes = 0
myDicTionary = {}


with open(inputFilePath,newline = '') as csvFile:
    csvContent = csv.reader(csvFile,delimiter = ",")
    csvHeader = next(csvContent)
    for row in csvContent:
        totalVotes+=1
        if row[2] not in myDicTionary:
            myDicTionary[row[2]] = 1 
        else:
            myDicTionary[row[2]] += 1
            
            #if row[2] not in myDicTionary.keys():
            
nameOutput = "electionResults.txt"
outputPath = os.path.join(nameOutput)
with open(outputPath,'w') as outFile:
    
    for key in myDicTionary.keys():
        print(f'Candidate: {key} - Had: {myDicTionary[key]/totalVotes*100.0:.0f} percent of the votes ({myDicTionary[key]})\n')
        outFile.write(f'Candidate: {key} - Had: {myDicTionary[key]/totalVotes*100.0:.0f} percent of the votes ({myDicTionary[key]})\n')
    print(f'The winner is: {list(myDicTionary.keys())[list(myDicTionary.values()).index(max(myDicTionary.values()))]}')        
    outFile.write(f'The winner is: {list(myDicTionary.keys())[list(myDicTionary.values()).index(max(myDicTionary.values()))]}')


    
    