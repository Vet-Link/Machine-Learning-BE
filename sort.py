import pandas as pd
from datetime import datetime
import csv
import json


def csv_to_json(file_path):
    json_array = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)

        for row in csv_reader:
            json_object = {}
            for header, value in zip(headers, row):
                # Remove leading and trailing spaces from the header and value
                header = header.strip()
                value = value.strip()

                # Convert specialty field back to array if it contains commas and spaces
                if header == 'specialty' and ',' in value:
                    value = [item.strip() for item in value.split(',')]

                json_object[header] = value
            json_array.append(json_object)

    return json_array


# Get today's date
today_date = datetime.today().strftime('%d_%m_%Y')

# Define the types
types = ['aquatic', 'pet', 'cattle', 'bird', 'exotic', 'reptile']

# Read and process data for each type
for type in types:
    # Construct the file path using today's date and type
    file_path = f"/home/Ezekiel/autorun/{today_date}/recommendations/{type}.csv"

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Separate existing and newcomer entries
    existing_entries = df[df['newcomer_status'] == 'EXISTING']
    newcomer_entries = df[df['newcomer_status'] == 'NEWCOMER']

    # Sort the DataFrame of newcomer entries by 'score' column in descending order
    df_sorted_newcomer = newcomer_entries.sort_values(by='score', ascending=False)

    # Add a new column 'rank' based on the rank of each entry
    df_sorted_newcomer['rank'] = df_sorted_newcomer['score'].rank(method='dense', ascending=False)

    # Sort the DataFrame of existing entries by 'score' column in descending order
    df_sorted_existing = existing_entries.sort_values(by='score', ascending=False)

    # Add a new column 'rank' based on the rank of each entry
    df_sorted_existing['rank'] = df_sorted_existing['score'].rank(method='dense', ascending=False)

    # Merge the sorted newcomer and existing entries back into the original DataFrame
    df = pd.concat([df, df_sorted_newcomer, df_sorted_existing]).drop_duplicates(subset=['vet_name'], keep='last')

    # Convert 'rank' column to integer type
    df['rank'] = df['rank'].astype(int)

    # Print the DataFrame to verify the changes
    print(df)

    # Construct the result file path using today's date, type, and 'manipulated_data' suffix
    result_file_path = f"/home/Ezekiel/autorun/{today_date}/json/manipulated_{type}_data.json"

    # Write the result to a new JSON file
    df_selected_columns = df[['rank', 'vet_name', 'newcomer_status']]
    json_data = df_selected_columns.to_dict(orient='records')
    with open(result_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
