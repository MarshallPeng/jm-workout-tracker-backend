from src.model.Workout import Workout
import uuid

class WorkoutService:

    def __init__(self, firebase_client):
        self.firebase_client = firebase_client
        self.target_workout = None


    def new_workout(self, user, name, category, is_repeated, date):
        """
        Create new workout object
        :param user:
        :param name:
        :param category:
        :param is_repeated:
        :param date:
        :return:
        """
        id = 'workout_' + str(uuid.uuid1())
        workout = Workout(id, user, name, [], category, is_repeated, date)
        self.target_workout = workout

    def load_workout(self, user, id):
        """
        Load workout from firebase
        :param user:
        :param id:
        :return:
        """
        self.target_workout = self.firebase_client.get_workout(user, id)

    def add_exercise(self, exercise):
        """
        Add exercise to workout
        :param exercise:
        :return:
        """
        if self.target_workout is not None and type(self.target_workout) is Workout:
            self.target_workout.add_exercise(exercise)


    def save_workout(self):
        """
        Commit workout to database.
        :return:
        """
        self.firebase_client.set_workout(self.target_workout.user, self.target_workout)


    def edit_info(self, field, value):
        """
        Edit the info of the workout (Not Exercises)
        :param field:
        :param value:
        :return:
        """

        self.target_workout.FIELD_NAMES[field](self.target_workout, value)







