import os
import csv
election_csv = os.path.join('Resources', 'election_data.csv')

poll = {}
total_votes = 0

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
candidates = []
votes = []
for key, value in poll.items():
    candidates.append(key)
    votes.append(value)

percentage = []
for vote in votes:
    percentage.append(round(vote/total_votes * 100, 3))
 
result = list(zip(candidates, votes, percentage))
winners = []
for name in result:
    if max(votes) == name[1]:
        winners.append(name[0])
winner = winners[0]
if len(winners) > 1:
    for w in range(1, len(winners)):
        winner = winner + "," + winners[w]

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes} ")
print("--------------------")
for each in result:
    print(each[0] + ": " + str(each[2]) + "% " + "(" + str(each[1]) + ")")
print(f"Winner: {winner}")
print("--------------------")

output_file = os.path.join('analysis', "PyPoll_Final.txt")
with open(output_file, "w") as datafile:
    datafile.write("Election Results")
    datafile.write("----------------------")
    datafile.write(f"Total Votes: {total_votes} ")
    datafile.write("-----------------------")
    for each in result:
        datafile.write(each[0] + ": " + str(each[2]) + "% " + "(" + str(each[1]) + ")")
    datafile.write(f"Winner: {winner} ")
    datafile.write("----------------------")
