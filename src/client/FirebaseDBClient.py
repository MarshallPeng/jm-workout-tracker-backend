import json

import firebase_admin
from firebase_admin import db, credentials

from src.config.config import FirebaseConfig
from src.constants.DatabaseConstants import DatabaseConstants


class FirebaseDBClient():

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH

        self.cred = credentials.Certificate(self.SDK_PATH)

        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(self.cred, {
                'databaseURL': FirebaseConfig.DATABASE_URL
            })

        self.db = db.reference()

    def add_user(self, user):
        self.db.push(DatabaseConstants.USERS, user)

    def set_user(self, user):
        self.db.child(DatabaseConstants.USERS + '/' + user.id).set(json.loads(user.toJSON()))

    def get_user_by_id(self, id):
        return self.db.child(DatabaseConstants.USERS + '/' + id).get()

    def delete_user(self, user):
        self.db.child(DatabaseConstants.USERS + '/' + user.id).delete()

    def delete_user_by_id(self, id):
        self.db.child(DatabaseConstants.USERS + '/' + id).delete()

    #for jake: for now use set_workout
    # def add_workout(self, user, workout):
    #     self.db.push(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS)

    def add_workout(self, userid, workoutid, workout):
        path = DatabaseConstants.get_workout_path(userid, workoutid)
        if self.db.child(path).get() is None:
            self.db.child(path).set([json.loads(workout.toJSON())])
        else:
            exercises = self.db.child(path).get()
            exercises.append(json.loads(workout.toJSON()))
            self.db.child(path).set(exercises)

    def delete_workout(self, user, workout):
        self.db.child(DatabaseConstants.USERS + '/' + user.id + '/' + DatabaseConstants.WORKOUTS + + workout.name)

    def get_workout(self, user, workout):
        #TODO: after UUID implemented, have get_workout_by_id method and get_by_name prob
        return self.db.child(
            DatabaseConstants.USERS + '/' + user.id + '/' + DatabaseConstants.WORKOUTS + + workout.id).get()

    def get_workout_by_id(self, userid, workoutid):
        return self.db.child(
            DatabaseConstants.USERS + '/' + userid + '/' + DatabaseConstants.WORKOUTS + '/' + workoutid).get()

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
