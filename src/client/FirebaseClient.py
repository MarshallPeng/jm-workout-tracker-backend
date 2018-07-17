import firebase_admin
from firebase_admin import db, credentials
from src.config.config import FirebaseConfig


class FirebaseClient:

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH

        self.cred = credentials.Certificate(self.SDK_PATH)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': FirebaseConfig.DATABASE_URL
        })
        self.db = db.reference()


    def set_workout(self, user, workout):
        self.db.child("Users/" + user + "/Workouts/").set(workout)


    def get_workout(self, user):
        return self.db.get("Users/" + user + "/Workouts/")

