import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = 0
candidate_list = []
candidate_dict = {}

winning_vote = 0 
winner = ""

with open("election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_dict[candidate] = 0

        candidate_dict[candidate] +=1 
   
    for candidate in candidate_dict: 
        percentage = round(float(candidate_dict[candidate])/float(total_votes) * 100,3)
        
        votes = candidate_dict[candidate]
        
        if votes > winning_vote:
            winning_vote = votes
            winner = candidate

with open("election_results.txt", "w") as txt_file:
    print("\nElection Results \n----------------------------")
    print(f"Total Months: {(total_votes)}\n----------------------------")
   
    # Need help with this!
    print(f"{candidate_dict}: {percentage:} ({candidate_dict[candidate]})\n")
    
    print(f"--------------------")
    print(f"Winner: {winner}")
    print(f"--------------------")

    txt_file.write("\nElection Results\n")
    txt_file.write("--------------------\n")
    txt_file.write(f"Total Months: {float(total_votes)}\n")
    txt_file.write("--------------------\n")
    
    # Need help with this!
    txt_file.write(f"{candidate_dict}: {percentage:} ({candidate_dict[candidate]})\n")
    
    txt_file.write("--------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("--------------------")

