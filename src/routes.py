
from firebase import Firebase
import os 


secret = os.getenv("firebase_storage")

config = {
    "apiKey": secret,
    "authDomain": "translateme-4f1db.firebaseapp.com",
    'databaseURL': "gs://translateme-4f1db.appspot.com",
    "projectId": "translateme-4f1db",
    "storageBucket": "translateme-4f1db.appspot.com",
    "messagingSenderId": "7171255240",
    "appId": "1:7171255240:web:5f40ce76b4bbe04674eefd",
    "measurementId": "G-GHTBKH6K4M"
}


