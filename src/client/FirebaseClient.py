import firebase_admin
from firebase_admin import db, credentials
from src.config.config import FirebaseConfig
from src.constants.DatabaseConstants import DatabaseConstants
from src.model.Exercise import Exercise
from src.model.Workout import Workout
from src.model.User import User

class FirebaseClient:

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH

        self.cred = credentials.Certificate(self.SDK_PATH)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': FirebaseConfig.DATABASE_URL
        })
        self.db = db.reference()

    def set_workout(self, user, workout):
        self.db.child(DatabaseConstants.USERS + user + DatabaseConstants.WORKOUTS).set(workout)

    def get_workout(self, user):
        return self.db.get(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS)

    def delete_workout(self, user):
        self.db.get_workout(user).delete()

    def set_exercise(self, user, workout, exercise):
        self.db.child(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants.EXERCISES).set(
            exercise)

    def get_exercise(self, user, workout):
        return self.db.get(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants)

    def delete_exercise(self, user, workout):
        self.db.get_exercise(self, user, workout).delete()



