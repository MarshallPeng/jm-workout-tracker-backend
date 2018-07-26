import uuid
import logging
from src.client.FirebaseClient import FirebaseClient
from src.model.User import User

class UserService:

    def __init__(self, firebase_client, target_user=None):
        if type(firebase_client) is FirebaseClient:
            self.firebase_client = firebase_client

        self.target_user = target_user


    def initialize_user(self, first_name, last_name):
        """
        Create new user with required fields first and last name.
        Also generate a uuid for that user.
        :param first_name:
        :param last_name:
        :return:
        """
        id = 'user_' + str(uuid.uuid1())
        new_user = User(id, first_name, last_name)
        self.target_user = new_user

    def load_user(self, id):
        """
        Load user from firebase given id
        :param id:
        :return:
        """
        self.target_user = self.firebase_client.get_user(id)


    def edit_user_info(self, id, field, value):

        """
        Modify User info given field name and value
        :param id:
        :param field: predefined by
        :param value:
        :return:
        """

        self.target_user.field_names[field](self.target_user, value)


    def edit_user_workouts(self):
        print "Do Something"


    def save_user(self, user):
        if self.target_user != None:
            self.firebase_client.add_user(user)
        else:
            logging.info("Can't save null user")

        return self.target_user





