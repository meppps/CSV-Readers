# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(f"Title: {row[0]}") 
            print(f"Rating: {row[1]}") 
            print(f"Released: {row[5]}") 
            print(f"Critic Score: {row[6]}")

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry, we cannot find what you are looking for.")

