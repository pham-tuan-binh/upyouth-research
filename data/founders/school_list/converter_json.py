import csv
import json

# Initialize an empty dictionary to store the data
data_map = {}

# Read the CSV file
with open('rated_school_list.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='@')
    
    # Skip the header row if it contains column names
    next(csvreader, None)

    # Iterate through the rows in the CSV file
    for row in csvreader:
        school, score = row[0], int(row[1])
        
        # Check if the score is already a key in the dictionary
        if score in data_map:
            data_map[score].append(school)
        else:
            data_map[score] = [school]

# Specify the path for the JSON output file
output_file_path = 'output.json'

# Write the JSON data to the output file
with open(output_file_path, 'w') as jsonfile:
    json.dump(data_map, jsonfile, indent=4)

print(f"JSON data has been written to {output_file_path}")