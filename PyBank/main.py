#import library
import os
import csv

#joining path(had to google this because how it was shown in class did not work for me)
budget_csv = os.path.join("/Users/lorenaolalde-rios/Documents/GitHub/python-challenge/PyBank/budget_data.csv")

# open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

     # define
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    
    #number of months in total
    total_months = len(months)
    
    # change in revenue
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    # average data revenue
    revenue_average = round(sum(revenue_change) / len(revenue_change),2)

    # increase and decrease in revenue
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)


    # output results
    print("Financial Analysis")

    print("----------------------------")
   
    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(P)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

    #output text file
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()