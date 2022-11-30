import os
import csv

pollData = os.path.join("..","Resources","election_data.csv")

with open(pollData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader) #skip header
    data = list(csvreader) #make unique
    row_count = len(data) #Count

    canidatelist = list() 
    votecount = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        votecount.append(candidate)
        if candidate not in canidatelist: 
            canidatelist.append(candidate)
    canidatecount = len(canidatelist)

    votes = list()
    percentage = list()
    for i in range (0,canidatecount):
        name = canidatelist[i]
        votes.append(votecount.count(name))
        votepercent = votes[i]/row_count
        percentage.append(votepercent)

    winner = votes.index(max(votes))    

  # Terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for i in range (0,canidatecount): 
        print(f"{canidatelist[i]}: {percentage[i]:.3%} ({votes[i]:,})")
    print("----------------------------")
    print(f"Winner: {canidatelist[winner]}")
    print("----------------------------")

  #Text File
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for i in range (0,canidatecount): 
        print(f"{canidatelist[i]}: {percentage[i]:.3%} ({votes[i]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {canidatelist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))