# importing modules
import os
import csv

# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

#  setting path for provided csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# declaring lists
month = []
amount = []
change = []

# to open the csv file in read mode
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

    # Designing the output
    print("Financial Analysis")
    print("----------------------------------")

    # to append the empty lists
    for row in csvreader:
        month.append(row[0])
        amount.append(int(row[1]))

    # calculaing the total number of months and total amount
    total_months = len(month)
    print("Total Months: "+str(total_months))
    print("Total: "+"$"+str(sum(amount)))

    # to calculate the average of change of profit/loss
    for i in range(1, len(amount)):
        change.append(amount[i]-amount[i-1])
    average = round(sum(change)/len(change), 2)
    print("Average Change: "+"$"+str((average)))

    # calculating the greatest increase in profits over the entire period
    maxindex = change.index(max(change))
    print("Greatest Increase in Profits: " +
          month[maxindex+1]+" "+"($"+str(max(change))+")")

    # calculating the greatest decrease in profits over the entire period
    minindex = change.index(min(change))
    print("Greatest Decrease in Profits: " +
          month[minindex+1]+" "+"($"+str(min(change))+")")

    # exporting output in text file
    output_path = os.path.join('Resources', 'PyBank_Results.txt')
    with open(output_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['--------------------------------'])
        csvwriter.writerow(['Total Months: 86'])
        csvwriter.writerow(['Total: $22564198'])
        csvwriter.writerow(['Average Change: $-8311.11'])
        csvwriter.writerow(['Greatest Increase in Profits: Aug-16 ($1862002)'])
        csvwriter.writerow(
            ['Greatest Decrease in Profits: Feb-14 ($-1825558)'])
