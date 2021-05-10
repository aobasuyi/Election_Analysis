# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# # Using the with statement open the file as a text file.
#     with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     #txt_file.write("Hello World ")

#     # Write three counties to the file.
#         txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")


# # Print the file object.
    #  print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()


# The data we need to retrieve.
# 1.The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidtae won
# 4. The total numer of votes each candidtae won
# 5. The winner of the election based on popular vote.

