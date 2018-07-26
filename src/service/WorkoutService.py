from src.model.Workout import Workout

class WorkoutService:

    def __init__(self, firebase_client):
        self.firebase_client = firebase_client


    def create_workout(self, user, name, exercises, category, is_repeated, date):
        workout = Workout(user, name, exercises, category, is_repeated, date)
        self.firebase_client.set_workout(workout)







