import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')


total_months = 0
prev_rev = 0
mon_cng = []
rev_cngs = []
grt_inc = ["", 0]
grt_dec = ["", 999999999]
total_rev = 0
rev_avg = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_months = total_months + 1
        total_rev = total_rev + int(row[1])
        rev_cng = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        
        rev_cngs = rev_cngs + [rev_cng]
      
        mon_cng = mon_cng + [row[0]]
        if (rev_cng > grt_inc[1]):
            grt_inc[0] = row[0]
            grt_inc[1] = rev_cng
        if (rev_cng < grt_dec[1]):
            grt_dec[0] = row[0]
            grt_dec[1] = rev_cng
    rev_cngs.pop(0)
    rev_avg = round(sum(rev_cngs)/len(rev_cngs),2)
     
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: $ {total_rev}")
    print(f"Average Change: ${rev_avg}")
    print(f"Greatest Increase in Profits: {grt_inc[0]} (${grt_inc[1]})")
    print(f"Greatest Decrease in Profits: {grt_dec[0]} (${grt_dec[1]})")
        
output_file = os.path.join('analysis', "PyBank_Final.txt")
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis")
    datafile.write("------------------------")
    datafile.write(f"Total Months: {total_months}")
    datafile.write(f"Total: $ {total_rev}")
    datafile.write(f"Average Change: ${rev_avg}")
    datafile.write(f"Greatest Increase in Profits: {grt_inc[0]} (${grt_inc[1]})")
    datafile.write(f"Greatest Decrease in Profits: {grt_dec[0]} (${grt_dec[1]})")