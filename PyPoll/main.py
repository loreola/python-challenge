#import library
import os
import csv
#join path
election_csv = os.path.join("/Users/lorenaolalde-rios/Documents/Data Analytics Work/Challenge 3/PyPoll/Resources/election_data.csv")


#open and read csv file and skipfirt row
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    cvsheader = next(csvfile)
    #define
    data = list(csvreader)
    row_count = len(data)

    #create list of candidates who receive votes
    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)

    #percetange of votes and total votes
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

    #winner by popular vote
    winner = votes.index(max(votes))    

    #print resuls
    print("Election Results")
    
    print("----------------------------")
   
    print(f"Total Votes: {row_count:}")
   
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:})")
    print("----------------------------")
   
    print(f"Winner: {candilist[winner]}")
   
    print("----------------------------")

    #output txt file
    print("Election Results", file=open("PyPoll.txt", "a"))
    
    print("----------------------------", file=open("PyPoll.txt", "a"))
    
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
   
    print("----------------------------", file=open("PyPoll.txt", "a"))
    
    print(f"Winner: {candilist[winner]}", file=open("PyPoll.txt", "a"))
    
    print("----------------------------", file=open("PyPoll.txt", "a"))
