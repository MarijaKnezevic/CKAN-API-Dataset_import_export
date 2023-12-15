import os
import requests
import json
import re

# CKAN API endpoint for searching datasets (here you need to add from which catalog you want to export dataset)
url = 'https://localhost:5000/api/3/action/package_search'

# Prompt the user if they want to export all datasets
export_all = input("Do you want to export all datasets? (yes/no): ").lower() == 'yes'

# Initialize num_datasets
num_datasets = 0

if not export_all:
    # Prompt the user for the number of datasets to export
    try:
        num_datasets = int(input("Enter the number of datasets to export: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

# Parameters for the search
params = {
    'q': '*:*',  # Search query to retrieve all datasets
    'start': 0,
    'rows': 10,  # Number of datasets to retrieve per request (adjust as needed)
}

# Create the 'export' folder if it doesn't exist
export_folder = 'export'
os.makedirs(export_folder, exist_ok=True)

def clean_filename(filename):
    # Remove or replace invalid characters in the filename
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def ask_overwrite(existing_filename, new_filename):
    response = input(f"Dataset '{existing_filename}' already exists. Do you want to overwrite it? (yes/no): ").lower()
    return response == 'yes'

datasets_exported = 0

while True:
    # Making the API request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting the list of datasets from the response
        datasets = response.json().get('result', {}).get('results', [])

        if not datasets:
            break  # No more datasets to retrieve

        # Save each dataset to a separate JSON file in the 'export' folder
        for dataset in datasets:
            if export_all or (not export_all and datasets_exported < num_datasets):
                dataset_title = dataset.get('title', 'unknown_title')
                dataset_title_cleaned = clean_filename(dataset_title)
                dataset_filename = os.path.join(export_folder, f'{dataset_title_cleaned}.json')

                # Check if the file already exists
                if os.path.exists(dataset_filename):
                    if ask_overwrite(dataset_filename, dataset_title_cleaned):
                        with open(dataset_filename, 'w') as dataset_file:
                            json.dump(dataset, dataset_file, indent=2)
                        print(f"Dataset '{dataset_title}' overwritten in {dataset_filename}")
                    else:
                        # Append a unique index to the filename
                        index = 1
                        while os.path.exists(dataset_filename):
                            dataset_filename = os.path.join(export_folder, f'{dataset_title_cleaned}_{index}.json')
                            index += 1

                        with open(dataset_filename, 'w') as dataset_file:
                            json.dump(dataset, dataset_file, indent=2)
                        print(f"Dataset '{dataset_title}' exported to {dataset_filename}")
                else:
                    with open(dataset_filename, 'w') as dataset_file:
                        json.dump(dataset, dataset_file, indent=2)
                    print(f"Dataset '{dataset_title}' exported to {dataset_filename}")

                datasets_exported += 1

        # Move to the next set of datasets
        params['start'] += params['rows']

        if not export_all and datasets_exported >= num_datasets:
            break  # Stop if the desired number of datasets is reached

    else:
        print(f"Error: {response.status_code}, {response.text}")
        break