from firebase_admin import auth, credentials
import firebase_admin

# TODO: Figure out how session tokens and shit work
from src.config.config import FirebaseConfig


class FirebaseAuthClient():

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH
        self.cred = credentials.Certificate(self.SDK_PATH)

        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(self.cred)

        self.auth = auth

    def register(self, email, phone, password, display_name):
        user = auth.create_user(
            email= email,
            phone_number = phone,
            password=password,
            display_name=display_name
        )

        print "created user with id: " + user.uid
        return user
