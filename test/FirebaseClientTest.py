
import unittest
from src.model.Exercise import Exercise
from src.model.Workout import Workout
from src.model.User import User
from src.client.FirebaseClient import FirebaseClient

class FirebaseClientTest(unittest.TestCase):
    exercise = None
    workout = None
    user = None
    def set_up(self):
        self.exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        self.workout = Workout("the day!!", 0, 0, 0, 0)
        self.user = User("Jake")
    def test_add_user(self):
        self.setUp()
        FirebaseClient.add_user()



    if __name__ == "__main__":
        main()