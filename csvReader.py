import csv
import os

#!/usr/bin/env python3

import cgi

print("Content-type: text/html\n")
form = cgi.FieldStorage()
user_email = form.getvalue('userEmail')

headerName = form.getvalue('preference')

#keyword = #Thing collected from the dropdown
#email = #Email typed in

def getPreferenceByEmail(csv_file, email, header_name):
    preference = None

    # Check if the file exists
    if not os.path.isfile(csv_file):
        print(f"Error: The file '{csv_file}' does not exist.")
        return preference

    # Open the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Use DictReader to work with headers
        found = False

        # Iterate through each row in the CSV file
        for row in reader:
            if row.get('Email') == email:
                preference = row.get(header_name)
                found = True
                break

    if not found:
        print(f"No entry found for email: {email}")
    
    return preference



def collect_rows_with_keyword(csv_file, keyword):
    collected_data = []
    keyword_lower = keyword.lower()  # Convert the keyword to lowercase

    # Check if the file exists
    if not os.path.isfile(csv_file):
        print(f"Error: The file '{csv_file}' does not exist.")
        return collected_data

    # Open the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the header row

        # Iterate through each row in the CSV file
        for row in reader:
            # Check if the keyword is present in any column of the row (case insensitive)
            if any(keyword_lower in cell.lower() for cell in row):
                collected_data.append(row)

    return headers, collected_data

preference = getPreferenceByEmail('shellHacksProject/tmp/devnodes.csv', user_email, headerName)

if __name__ == "__main__":
    # Define the CSV file with the full path
    csv_file = 'shellHacksProject/tmp/devnodes.csv'  # Update with your path

    # Optional: Print the current working directory
    print("Current Working Directory:", os.getcwd())

    # Prompt the user for the keyword
    keyword = preference

    # Collect rows that contain the keyword
    headers, result = collect_rows_with_keyword(csv_file, keyword)

    # Check if any data was collected
    if result:
        # Print the header
        print("\nCollected Data:")
        print("-" * 50)
        print(f"{' | '.join(headers)}")
        print("-" * 50)

        # Print the collected data
        for data in result:
            print(f"{' | '.join(data)}")
    else:
        print("No matching rows found.")

