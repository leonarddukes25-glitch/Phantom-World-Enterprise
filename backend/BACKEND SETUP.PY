import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key
cred = credentials.Certificate("SERVICEACCOUNTKEY.json")

# Initialize Firebase Admin
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Test read
def test_connection():
    docs = db.collection('testCollection').stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

if __name__ == "__main__":
    print("Testing Firebase backend connection...")
    test_connection()
