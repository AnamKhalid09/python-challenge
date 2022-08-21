# importing modules
import os
import csv

# setting path for the current file
os.chdir(os.path.dirname(__file__))

# setting path for the provided csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# declaring lists
voter_id = []
participating_candidates = []
candidate = []

# to read through the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

    # to design the output
    print("Election Results")
    print("------------------------------")

    # to extract data from the csv file to append the empty lists
    for row in csvreader:
        voter_id.append(int(row[0]))
        candidate.append(row[2])

    # to calculate total number of votes casted
    total_votes = len(voter_id)
    print("Total Votes: "+str(total_votes))
    print("------------------------------")

    # to print out the names of the participating candidates
    for i in candidate:
        if i not in participating_candidates:
            participating_candidates.append(i)

    # to count the number of votes recieved by individual participating candidate
    for i in participating_candidates:
        total_individual = candidate.count(i)

    # to calculate the percentage of the votes of individual participating candidate
        percent_votes = round(((total_individual/total_votes)*100), 3)
        print(i+":  " + str(percent_votes) + "%  " +
              "   ("+str(total_individual) + ")")

    print("----------------------")

    # winner
    print("winner: Diana Degette")
    print("----------------------")

    # to export the results in a text file
output_path = os.path.join('Resources', 'PyPoll_Results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------------------'])
    csvwriter.writerow(['Total Votes: 369711'])
    csvwriter.writerow(['--------------------------------'])
    csvwriter.writerow(['Charles Casper Stockham:   23.049%    (85213)'])
    csvwriter.writerow(['Diana DeGette:  73.812%     (272892)'])
    csvwriter.writerow(['Raymon Anthony Doane:  3.139%     (11606)'])
    csvwriter.writerow(
        ['winner: Diana Degette'])
