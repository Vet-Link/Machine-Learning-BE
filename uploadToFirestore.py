from google.cloud import firestore
from google.oauth2 import service_account
import json

# Load the service account key file
key_file = '/home/Ezekiel/autorun/service-key-firestore.json'

# Initialize Firestore client with specified database ID
credentials = service_account.Credentials.from_service_account_file(key_file)
db = firestore.Client(project='vetlink-425416', credentials=credentials, database='patient-db')

def store_data_regis(ID, user_data_regis):
    collection_ref = db.collection('doctor-data')
    collection_ref.document(ID).update(user_data_regis)

aquatic_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_aquatic_data.json'
with open(aquatic_file_data, 'r') as file:
    # Baca isi file JSON
    aquatic_json_data = json.load(file)

bird_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_bird_data.json'
with open(bird_file_data, 'r') as file:
    # Baca isi file JSON
    bird_json_data = json.load(file)

cattle_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_cattle_data.json'
with open(cattle_file_data, 'r') as file:
    # Baca isi file JSON
    cattle_json_data = json.load(file)

exotic_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_exotic_data.json'
with open(exotic_file_data, 'r') as file:
    # Baca isi file JSON
    exotic_json_data = json.load(file)

pet_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_pet_data.json'
with open(pet_file_data, 'r') as file:
    # Baca isi file JSON
    pet_json_data = json.load(file)

reptile_file_data = '/home/Ezekiel/autorun/20_06_2024/json/manipulated_reptile_data.json'
with open(reptile_file_data, 'r') as file:
    # Baca isi file JSON
    reptile_json_data = json.load(file)


for i in range(len(aquatic_json_data)):
    if aquatic_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(aquatic_json_data[i]['vet_name'], { 'aquaticRank': aquatic_json_data[i]['rank'], 'newcomer_status': newcomer_status })

for i in range(len(bird_json_data)):
    if bird_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(bird_json_data[i]['vet_name'], { 'birdRank': bird_json_data[i]['rank'], 'newcomer_status': newcomer_status })

for i in range(len(cattle_json_data)):
    if cattle_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(cattle_json_data[i]['vet_name'], { 'cattleRank': cattle_json_data[i]['rank'], 'newcomer_status': newcomer_status })

for i in range(len(exotic_json_data)):
    if exotic_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(exotic_json_data[i]['vet_name'], { 'exoticRank': exotic_json_data[i]['rank'], 'newcomer_status': newcomer_status })

for i in range(len(pet_json_data)):
    if pet_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(pet_json_data[i]['vet_name'], { 'petRank': pet_json_data[i]['rank'], 'newcomer_status': newcomer_status })

for i in range(len(reptile_json_data)):
    if reptile_json_data[i]['newcomer_status'] == 'NEWCOMER':
        newcomer_status = True
    else :
        newcomer_status = False
    store_data_regis(reptile_json_data[i]['vet_name'], { 'reptileRank': reptile_json_data[i]['rank'], 'newcomer_status': newcomer_status })