import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    csv_header = next(csvfile)
    print(f"Header {csv_header}")

    for row in csvreader:

        if float(row[7]) >= 5:
            print(row)
        




 