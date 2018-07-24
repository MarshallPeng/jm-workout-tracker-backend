import os

class FirebaseConfig:

    DATABASE_URL = 'https://jm-workout-tracker.firebaseio.com/'
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    SDK_PATH = PROJECT_ROOT + "/config/jm-workout-tracker-firebase-adminsdk.json"

