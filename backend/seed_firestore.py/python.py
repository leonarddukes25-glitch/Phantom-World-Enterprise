import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account (you had it at BACKEND/CONFIG/FIREBASE-KEY.json)
cred = credentials.Certificate("CONFIG/FIREBASE-KEY.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def seed():
    # collection: testCollection, doc id: hello
    doc = {
        "msg": "Dynasty online",
        "env": "prod",
        "by": "seed_script"
    }
    db.collection("testCollection").document("hello").set(doc)
    print("Seeded: testCollection/hello =>", doc)

if __name__ == "__main__":
    seed()
