import json

# Path ke file JSON
file_path = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_aquatic_data.json'

# Buka file JSON
with open(file_path, 'r') as file:
    # Baca isi file JSON
    data = json.load(file)

print(data[0]['rank'])