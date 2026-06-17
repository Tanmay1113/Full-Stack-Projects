import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load .env
load_dotenv()

# Firebase key path
FIREBASE_KEY = os.getenv("FIREBASE_KEY", "serviceAccountKey.json")

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_KEY)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
