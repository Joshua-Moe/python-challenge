#!/usr/bin/env python3

import os

""" Module 3 Challenge

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote


"""

def PyPoll():
    election_dict = {}
    file = os.path.join("Resources","election_data.csv")
    with open(file, 'r') as fh:
        lines = fh.readlines()
        header = lines[0] # I don't need the header for this; for the grading ruberic.
        for line in lines[1:]:
            ballot_ID, County, Candidate = line.strip().split(",")
            election_dict[Candidate] = election_dict.get(Candidate, 0) + 1
        
        # The total votes cast
        totalVotes = sum(list(election_dict.values()))
        
        # A complete list of candidates who received votes
        candidate_list = list(election_dict.keys())
        # print(len(candidate_list)) --> There are only 3 candidates
        
        # The percentage of votes each candidate won
        vote_stat_dict = {}
        for key,value in election_dict.items():
            vote_stat_dict[key] = round((value/totalVotes)*100, 3)
        
        # The total number of votes each candidate won
        tuple_list = []
        for key,value in election_dict.items():
            tuple_list.append((value, key))
        tuple_list.sort(reverse=True)
        
        # The winner of the election based on popular vote
        winner = tuple_list[0][1]
        
        
        results = "Election Results\n\n" + "-------------------------\n\n"
        results += f"Total Votes: {totalVotes}\n\n"
        results += "-------------------------\n\n"
        results += f"{candidate_list[0]}: {vote_stat_dict[candidate_list[0]]}% ({election_dict.get(candidate_list[0])})\n\n"
        results += f"{candidate_list[1]}: {vote_stat_dict[candidate_list[1]]}% ({election_dict.get(candidate_list[1])})\n\n"
        results += f"{candidate_list[2]}: {vote_stat_dict[candidate_list[2]]}% ({election_dict.get(candidate_list[2])})\n\n"
        results += "-------------------------\n\n"
        results += f"Winner: {winner}\n\n"
        results += "-------------------------\n\n"
        print(results)
    
    # Saving to output file
    output_path = os.path.join("analysis","PyPoll_output.txt")
    with open(output_path,'w') as fh:
        fh.write(results)
    
    
if __name__=="__main__":
    PyPoll()
