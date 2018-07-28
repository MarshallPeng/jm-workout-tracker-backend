from firebase_admin import credentials
import firebase_admin
from firebase_admin import db, credentials, auth
import json

from src.constants.DatabaseConstants import DatabaseConstants
from src.config.config import FirebaseConfig


class FirebaseClient:

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH
        self.cred = credentials.Certificate(self.SDK_PATH)

        firebase_admin.initialize_app(self.cred, {
            'databaseURL': FirebaseConfig.DATABASE_URL
        })

        self.db_client = FirebaseDBClient()
        self.auth_client = FirebaseAuthClient()
