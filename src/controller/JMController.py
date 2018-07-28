from flask import Flask, jsonify
import logging

from src.client.FirebaseDBClient import FirebaseDBClient
from src.service.UserService import UserService
from src.service.WorkoutService import WorkoutService


class JMController:

    def __init__(self):
        self.firebase_db_client = FirebaseDBClient()
        self.user_service = UserService(self.firebase_db_client)
        self.workout_service = WorkoutService(self.firebase_db_client)



    def get_user(self, id):
        result = self.user_service.load_user(id)
        logging.info(result)
        response = result.toJSON()
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    # TODO: initialize user needs to go through auth first.
    def register(self, first_name, last_name):
        self.user_service.initialize_user(first_name, last_name)
        logging.info("User initialized with id: " + 1)
        self.user_service.save_user()


