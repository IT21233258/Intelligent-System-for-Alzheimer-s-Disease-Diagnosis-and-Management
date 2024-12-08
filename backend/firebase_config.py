import firebase_admin
from firebase_admin import credentials, firestore

# Path to the Firebase private key (JSON file)
cred = credentials.Certificate("C:/Users/USER/Desktop/Emotion Recognition/backend/firebase-key.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
