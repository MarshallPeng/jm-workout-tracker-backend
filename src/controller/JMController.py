from flask import Flask, jsonify, Response
import logging

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.service.UserService import UserService
from src.service.UserServiceException import UserServiceException
from src.service.WorkoutService import WorkoutService
from src.util.ResponseUtil import ResponseUtil


class JMController:

    def __init__(self):
        self.firebase_db_client = FirebaseDBClient()
        self.auth = FirebaseAuthClient()
        self.user_service = UserService(self.firebase_db_client, self.auth)
        self.workout_service = WorkoutService(self.firebase_db_client)
        self.response_util = ResponseUtil()


    def get_user(self, id):
        result = self.user_service.load_user_by_id(id)
        logging.info(result)
        response = result.toJSON()
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    # TODO: initialize user needs to go through auth first.
    def register(self, data):

        # get data from POST request
        try:
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            phone_number = data['phone_number']
            password = data['password']

        # check for missing fields
        except KeyError as e:
            message = "required field \'" + e.message + "\' not found"
            response = self.response_util.build_error_response(code=400, message=message)
            return response

        logging.info("Attempting to initialize user...")

        # Attempt to initialize user
        try:
            user = self.user_service.initialize_user(
                first_name= first_name,
                last_name= last_name,
                email= email,
                phone_number= phone_number,
                password=password
            )

        # Catch any errors from UserServiceException
        except UserServiceException as e:
            logging.error(e.developer_message)
            response = self.response_util.build_error_response(code=e.status_code, message=e.message)
            return response

        # Return success message.
        logging.info("User initialized with id: " + user.id)
        response = self.response_util.build_success_response(code=201, message='User Created', data = user.toJSON())
        return response


    # def add_workout(self, data):
    #
    #
    #     user = self.user_service.load_user_by_id(id)
    #     self.workout_service.new_workout(
    #         user=user,
    #         name=workout_name,
    #         category=category,
    #         is_repeated
    #
    #     )
