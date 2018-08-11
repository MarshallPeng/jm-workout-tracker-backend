import uuid
import json
import logging

from firebase_admin.auth import AuthError

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseClient import FirebaseClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.model.User import User
from src.service.UserServiceException import UserServiceException
from src.service.WorkoutService import WorkoutService

import firebase_admin


class UserService:

    def __init__(self, db, auth, target_user=None):
        self.auth = auth
        self.db = db
        self.target_user = target_user


    # TODO: Figure out how to authenticate a user/session info.
    def initialize_user(self, email, phone_number, password, first_name, last_name):
        """
        Create new user with required fields first and last name.
        Also generate a uuid for that user.
        :param first_name:
        :param last_name:
        :return:
        """
        display_name = first_name + " " + last_name

        try:
            user = self.auth.register(email, phone_number, password, display_name)
        except AuthError as e:
            server_response = json.loads(e.message.split('Server response:')[1])
            code = server_response['error']['code']
            user_message = server_response['error']['message']
            raise UserServiceException(e, user_message, e.message, status_code=code)

        new_user = User(
            id=user.uid,
            first_name=user.display_name.split(' ')[0],
            last_name=user.display_name.split(' ')[1],
            email=user.email,
            phone_number=user.phone_number
        )

        self.target_user = new_user
        self.db.set_user(new_user)
        return new_user

    def load_user_by_id(self, id):
        """
        Load user from firebase given id
        :param id:
        :return:
        """
        self.target_user = self.db.get_user_by_id(id)
        return self.target_user


    def edit_user_info(self, id, field, value):

        """
        Modify User info given field name and value
        :param id:
        :param field: predefined by
        :param value:
        :return:
        """

        self.target_user.FIELD_NAMES[field](self.target_user, value)


    def edit_user_workouts(self):
        print("Do Something")

    def delete_user(self, user):
        """
        Delete User through the User object
        :param user:
        :return:
        """
        self.auth.delete(user.id)
        self.db.delete_user(user)

    def delete_user_by_id(self, id):
        """
        Delete user through a UserId
        :param id:
        :return:
        """
        print("needed for tests")
        self.auth.delete(id)

    def save_user(self, user):
        if self.target_user != None:
            self.db.add_user(user)
        else:
            logging.info("Can't save null user")

        return self.target_user





