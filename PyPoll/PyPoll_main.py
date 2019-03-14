
import os
import csv

# Open and read csv
election_data_csv_path = os.path.join("Resources", "election_data.csv")
with open(election_data_csv_path, newline="", encoding='utf-8-sig') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    total_vote=0
    # set two dictionaries
    candi_dic_1 = {}
    candi_dic_2 ={}
    
    for row in csv_reader:
        # Total vote counts
        total_vote += 1
        # when we start to read the second row
        if total_vote >1:
            candi=row[2]
            # Store candidate name in dictionary(candi_dic_1) as key
            # store votes they win in dictionary(candi_dic_1) as value
            candi_dic_1[candi]=candi_dic_1.get(candi,0) + 1
            
total_vote -= 1
# Counting the percentage of votes each candidate won and convert it to string
# Store candidate name(key) and percentage(value) in the other dictionary(candi_dic_2)
for i in candi_dic_1:
    candi_dic_2[i]=str(round(candi_dic_1[i]/total_vote*100,0))+'00%'


# The list of candidates 
candi_name=list(candi_dic_1.keys()) 
print(f'We got {len(candi_name)} candidates\n')
# The list of votes each candidate won
candi_votes=list(candi_dic_1.values())
# The list of percentage of votes each candidate won
candi_votes_perce=list(candi_dic_2.values())
# Find the winner 
greatest_votes=max(candi_votes)
winner_name=candi_name[candi_votes.index(greatest_votes)]



print('Election Results')
print("----------------------------")
print(f'Total Votes: {total_vote}')
print("----------------------------")
print(f'{candi_name[0]}: {candi_votes_perce[0]} ({candi_votes[0]})')
print(f'{candi_name[1]}: {candi_votes_perce[1]} ({candi_votes[1]})')                
print(f'{candi_name[2]}: {candi_votes_perce[2]} ({candi_votes[2]})')                         
print(f'{candi_name[3]}: {candi_votes_perce[3]} ({candi_votes[3]})')
print("----------------------------")
print(f'Winner: {winner_name}')    


# Set path for the location of report txt file
output_path = os.path.join("Resources", "Election Results.txt")

# write the summary of analysis to 'vote_analysis.txt"
outfile = open(output_path, "w")
outfile.write("Election Results\n")
outfile.write("----------------------------\n")
outfile.write(f"Total Votes: {total_vote}\n")
outfile.write("----------------------------\n")
outfile.write(f'{candi_name[0]}: {candi_votes_perce[0]} ({candi_votes[0]})')
outfile.write(f'{candi_name[1]}: {candi_votes_perce[1]} ({candi_votes[1]})')                
outfile.write(f'{candi_name[2]}: {candi_votes_perce[2]} ({candi_votes[2]})')                         
outfile.write(f'{candi_name[3]}: {candi_votes_perce[3]} ({candi_votes[3]})')
outfile.write("----------------------------")
outfile.write("----------------------------\n")
outfile.write(f'Winner: {winner_name}')

outfile.close()


                          
