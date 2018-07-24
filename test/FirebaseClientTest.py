
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
    def set_up(self):
        self.exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        self.workout = Workout("the day!!", 0, 0, 0, 0)
        self.user = User("Jake")
        self.firebase_client_test = FirebaseClient.__init__()
    def test_set_user(self):
        self.setUp()
        FirebaseClient.set_user(self.firebase_client_test, self.user)
        assert(FirebaseClient.get_usertemp0(self.firebase_client_test, self.user) is not None)
        assert(FirebaseClient.get_usertemp1(self.firebase_client_test, self.user) is not None)

    def main(self):
        self.set_up()
        self.test_add_user()

    if __name__ == "__main__":
        main()