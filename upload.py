from google.cloud import firestore
import json

# Load the service account key file
key_file = 'service-key-firestore.json'

# Authenticate with Firestore using the service account
db = firestore.Client.from_service_account_json(key_file)

def store_data_regis(ID, user_data_regis):
    collection_ref = db.collection('login-info')
    collection_ref.document(ID).set(user_data_regis)

# Example usage
if __name__ == "__main__":
    # Replace 'user-id' with the actual user ID
    user_id = 'user-id'

    # Replace this dictionary with the actual user data to be stored
    user_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    }

    store_data_regis(user_id, user_data)
    print(f"Data for user {user_id} has been stored.")
