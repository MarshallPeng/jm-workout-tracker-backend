class DatabaseConstants:
    USERS = "Users"
    WORKOUTS = "Workouts"
    EXERCISES = "Exercises"

    @staticmethod
    def get_workout_path(userid, workoutid):
        return DatabaseConstants.USERS + '/' + userid + '/' + DatabaseConstants.WORKOUTS + '/' + workoutid + '/' + DatabaseConstants.EXERCISES



