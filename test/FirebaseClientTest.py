import unittest

import firebase_admin

from src.client.FirebaseDBClient import FirebaseDBClient
from src.model.User import User
from src.model.Workout import Workout


class FirebaseClientTest(unittest.TestCase):
    """
    Tests for reading/writing from Firebase
    """

    def setUp(self):
        # self.exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        self.workout = Workout("workout_id", "workout_name", [], "workout_category", "workout_is_repeated", "Workout_date")
        self.user = User("test_id", "test_first_name", "test_last_name", None, None)
        self.firebase_test_client = FirebaseDBClient()


    def tearDown(self):
        firebase_admin.delete_app(firebase_admin.get_app())

    def test_set_user(self):
        """
        Check to see that user can be created and retrieved
        """

        self.firebase_test_client.set_user(self.user)
        retrieved = User.fromJSON(self.firebase_test_client.get_user_by_id(self.user.id))

        self.assertEqual(self.user, retrieved)


