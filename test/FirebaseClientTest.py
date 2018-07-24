
import unittest
from src.model.Exercise import Exercise
from src.model.Workout import Workout
from src.model.User import User
from src.client.FirebaseClient import FirebaseClient

class FirebaseClientTest(unittest.TestCase):
    exercise = None
    workout = None
    user = None
    firebase_client_test = None


    def setUp(self):
        self.exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        self.workout = Workout("the day!!", 0, 0, 0, 0)
        self.user = User("Jake")
        self.firebase_test_client = FirebaseClient()

    def test_set_user(self):
        """
        Check to see that user can be created
        """
        self.firebase_test_client.set_user(self.user)
        retrieved = self.firebase_test_client.get_user(self.user)

        self.assertEquals(self.user.__dict__, retrieved)