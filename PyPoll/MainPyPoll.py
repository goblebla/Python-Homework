import os
import csv

#Locating correct file path
csvpath = os.path.join('election_data.csv')

#Creating variables
totalvotes = 0
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0


#Open CSV file and store into variable
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Iterate and append through rows in stored csvfile
    for row in csvreader:
        
        #Count voter ID's
        totalvotes += 1

        #Count specific votes per candidate
        if row[2] == "Khan":
            khanvotes += 1
        elif row[2] == "Correy":
            correyvotes += 1
        elif row[2] == "Li":
            livotes += 1
        elif row[2] == "O'Tooley":
            otooleyvotes += 1

#Create dictionary of these 2 lists created to find winner
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khanvotes, correyvotes, livotes, otooleyvotes]

dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Summary of results
khanpercent = (khanvotes/totalvotes)*100
correypercent = (correyvotes/totalvotes)*100
lipercent = (livotes/totalvotes)*100
otooleypercent = (otooleyvotes/totalvotes)*100


#Create 
output = (
f"Election Results\n"
f"---------------------------\n"
f"Total Votes: {totalvotes}\n"
f"---------------------------\n"
f"Khan: {khanpercent:.3f}% ({khanvotes})\n"
f"Correy: {correypercent:.3f}% ({correyvotes})\n"
f"Li: {lipercent:.3f}% ({livotes})\n"
f"O'Tooley: {otooleypercent:.3f}% ({otooleyvotes})\n"
f"---------------------------\n"
f"Winner: {key}\n"
)

print(output)


#Output file path
textfile = os.path.join('PyPoll Voting Analysis File.txt')

with open(textfile, 'w') as txt_file:
    txt_file.write(output)


