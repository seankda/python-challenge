# Import Libraries
import csv
import os
# Suggested that 'import pathlib' would be better than 'import os'

# Declare variables
# Lists
months = []
revenue = []
monthlyChange = []

# File path
csvpath = os.path.join("PyBank","Resources","budget_data.csv")

# Open and read the csv 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    line = next(csvreader)

# Loop function, process rows
# Append rows to index 0
# Append rows to index 1
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

# Count total months
totalMonths = len(months)

# Find change in revenue per month
j = 0
k = 0
for j in range (0, totalMonths):
  if j == 0:
    monthlyChange.append(0)
  else: 
    monthlyChange.append(int(revenue[j])-int(revenue[k]))
    k += 1 

# Create the min, max and total revenue variables
# Check: Min, Max and Total revenues are all correct
maxVal = revenue[0]
minVal = revenue[0]
totalRevenue = 0

# The net total amount of "Profit/Losses" over the entire period
for r in range(len(revenue)):
    if revenue[r] >= maxVal:
        maxVal = revenue[r]
        maxValMon = months[r]
    elif revenue[r] <= minVal:
        minVal = revenue[r]
        minValMon = months[r]
    totalRevenue += revenue[r]

#Find min revenue change
minRevChange = min(monthlyChange)
minIndex = monthlyChange.index(minRevChange)
minDate = months[minIndex]

#Find max revenue change
maxRevChange = max(monthlyChange)
maxIndex = monthlyChange.index(maxRevChange)
maxDate = months[maxIndex]

# Get average change in monthly revenue
sumMonthlyChange = 0
tM = 0 
for tM in range(totalMonths):
  sumMonthlyChange = sumMonthlyChange + int(monthlyChange[tM])
averageChange = int(sumMonthlyChange)/int(totalMonths - 1)

# Print all results
print(f"""Pybank
Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalRevenue}
Average Change: ${averageChange:.2f}
Greatest Increase in Profits: {maxValMon} (${maxRevChange})
Greatest Decrease in Profits: {minValMon} (${minRevChange})
""")
# f""" is better than \n\. It accepts line breaks
# f string format is better than .format

# Checks:
# Total Months - CORRRECT
# Total - CORRECT
# Average Change - CORRECT
# Greatest Increase - CORRECT
# Greatest Decrease - CORRECT

# Note/Off-topic
# you may want to type
# if not x: if x has __bool__ dunder
# instead of "if found is False:
# "is" operator is mostly used for memory comparison between stuff