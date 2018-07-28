from firebase_admin import auth


# TODO: Figure out how session tokens and shit work.
# TODO:
class FirebaseAuthClient():

    def __init__(self):
        self.auth = auth

    def register(self):
        print "Do something"