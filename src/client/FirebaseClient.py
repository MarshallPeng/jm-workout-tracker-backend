import firebase_admin
import json
from firebase_admin import db, credentials
from src.config.config import FirebaseConfig
from src.constants.DatabaseConstants import DatabaseConstants

class FirebaseClient:

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH

        self.cred = credentials.Certificate(self.SDK_PATH)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': FirebaseConfig.DATABASE_URL
        })
        self.db = db.reference()

    def add_user(self, user):
        self.db.push(DatabaseConstants.USERS, user)

    def set_user(self, user):
        self.db.child(DatabaseConstants.USERS + '/' + user.id).set(json.loads(user.toJSON()))

    def get_user(self, user):
        return self.db.child(DatabaseConstants.USERS + '/' + user.id).get()

    #for jake: for now use set_workout
    def add_workout(self, user, workout):
        self.db.push(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS)

    def set_workout(self, user, workout):
        self.db.child(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout.title).set(workout.__dict)

    def delete_workout(self, user, workout):
        self.db.child(DatabaseConstants.USERS + '/' + user.id + '/' + DatabaseConstants.WORKOUTS + + workout.name)

    def get_workout(self, user, workout):
        #TODO: after UUID implemented, have get_workout_by_id method and get_by_name prob
        return self.db.child(
            DatabaseConstants.USERS + '/' + user.id + '/' + DatabaseConstants.WORKOUTS + + workout.name).get()

    def set_exercise(self, user, workout, exercise):
        #Marshall, would it be cleaner to call delete on the get_user() or is this fine?
        self.db.child(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants.EXERCISES).set(
            exercise).set(exercise.__dict__)

    def get_exercise(self, user, workout, exercise):
        return self.db.child(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants.EXERCISES + '/' + exercise.name).get()

    def delete_exercise(self, user, workout, exercise):
        self.db.child(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants.EXERCISES).set(
            exercise).set(user, workout, exercise).delete()



