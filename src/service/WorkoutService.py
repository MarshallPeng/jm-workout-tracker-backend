from src.model.Workout import Workout
import uuid

class WorkoutService:

    def __init__(self, firebase_client):
        self.db = firebase_client
        self.target_workout = None


    def new_workout(self, userid, name, category, is_repeated, date):
        """
        Create new workout object
        :param user:
        :param name:
        :param category:
        :param is_repeated:
        :param date:
        :return:
        """
        id = str(uuid.uuid1())
        workout = Workout(id, name, [], category, is_repeated, date)
        self.db.set_workout(userid, workout)
        self.target_workout = workout
        return workout

    def load_workout(self, userid, workoutid):
        """
        Load workout from firebase
        :param user:
        :param id:
        :return:
        """
        self.target_workout = self.db.get_workout_by_id(userid, workoutid)

    def add_exercise(self, exercise):
        """
        Add exercise to workout
        :param exercise:
        :return:
        """
        if self.target_workout is not None and type(self.target_workout) is Workout:
            self.target_workout.add_exercise(exercise)


    def save_workout(self, userid, workoutid, exercise):
        """
        Commit workout to database.
        :return:
        """

        self.db.add_workout(userid, workoutid, exercise)


    def edit_info(self, field, value):
        """
        Edit the info of the workout (Not Exercises)
        :param field:
        :param value:
        :return:
        """

        self.target_workout.FIELD_NAMES[field](self.target_workout, value)







