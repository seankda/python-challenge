# Import Libraries
import os
import csv

# Declare variables
# Lists
candidates = []
voteCounts = []
# Counter
voteCounter = 0

# File path
csvpath = os.path.join("PyPoll","Resources","election_data.csv")

# Open and read the csv 
with open(csvpath,newline="") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')

    # Skip header
    line = next(csvreader)

    # Process the votes
    for line in csvreader:

        # Add to vote counter
        voteCounter = voteCounter + 1

        candidate = line[2]

        # If candidate exists, add to vote count
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            voteCounts[candidate_index] = voteCounts[candidate_index] + 1
        # If candidate does not exist, create as new
        else:
            candidates.append(candidate)
            voteCounts.append(1)

# Stat vars
percentStat = []
maxVotes = voteCounts[0]
maxCounter = 0

# Calculate percentage per candidate
for count in range(len(candidates)):
    votePercent = voteCounts[count]/voteCounter*100
    percentStat.append(votePercent)
    if voteCounts[count] > maxVotes:
        maxVotes = voteCounts[count]
        maxCounter = count

# Winner
winner = candidates[maxCounter]

# Round decimal
percentStat = [round(i,2) for i in percentStat]  

# Print results
print(f"""  Election Results
  -------------------------
  Total Votes: {voteCounter}
  -------------------------""")
for count in range(len(candidates)):
   print(f"  {candidates[count]}: ${percentStat[count]:.3f}% ({voteCounts[count]})")
print(f"""  -------------------------
  Winner: {winner}
  -------------------------
""")

# Print to txt file
with open('PyPoll.txt','w',newline='') as txt_file:
    write2txt = csv.writer(txt_file)

    write2txt.writerow("  Election Results \n")