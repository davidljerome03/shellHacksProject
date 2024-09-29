import csv
import os

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

if __name__ == "__main__":
    # Define the CSV file with the full path
    csv_file = 'shellHacksProject/tmp/devnodes.csv'  # Update with your path

    # Optional: Print the current working directory
    print("Current Working Directory:", os.getcwd())

    # Prompt the user for the keyword
    keyword = input("Enter the keyword to search for: ")

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
