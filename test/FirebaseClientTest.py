import unittest
import firebase_admin
from src.client.FirebaseClient import FirebaseClient
from src.model.User import User
from src.model.Workout import Workout


class FirebaseClientTest(unittest.TestCase):

    def setUp(self):
        # self.exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        self.workout = Workout("workout_id", "workout_name", [], "workout_category", "workout_is_repeated", "Workout_date")
        self.user = User("test_id","test_first_name", "test_last_name", workouts=[self.workout])
        self.firebase_test_client = FirebaseClient()


    def tearDown(self):
        firebase_admin.delete_app(firebase_admin.get_app())

    def test_set_user(self):
        """
        Check to see that user can be created and retrieved
        """

        self.firebase_test_client.set_user(self.user)
        retrieved = User.fromJSON(self.firebase_test_client.get_user(self.user))

        self.assertEquals(self.user, retrieved)


