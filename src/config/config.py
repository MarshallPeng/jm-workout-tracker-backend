from pathlib import Path
class FirebaseConfig:

    DATABASE_URL = 'https://jm-workout-tracker.firebaseio.com/'
    SDK_PATH = Path("../src/config/").resolve()
    SDK_PATH = str(SDK_PATH.absolute()) + '/jm-workout-tracker-firebase-adminsdk.json'

