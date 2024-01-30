import os
import json

# Define the directory path you want to search
directory = "../data/founders"

founders = []

# Loop through each file in the directory
for filename in sorted(os.listdir(directory)):
    file_path = os.path.join(directory, filename)
    
    # Check if it's a file
    if os.path.isfile(file_path):
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                founders.append(data["full_name"])
                # Print the data, or do whatever processing you need
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file {filename}")


print(founders)  
