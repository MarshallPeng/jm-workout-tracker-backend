
import unittest
from src.model.Exercise import Exercise
from src.model.Workout import Workout
from src.model.User import User


class FirebaseClientTest(unittest.TestCase):

    def test(self):
        exercise = Exercise("Barbell curl", 135, 3, 12, 500, 11)
        workout = Workout("the day!!", 0, 0, 0, 0) 

    if __name__ == "__main__":
        main()