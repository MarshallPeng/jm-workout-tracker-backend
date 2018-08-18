from flask import Flask, jsonify, Response
import logging

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.model.Exercise import Exercise
from src.service.UserService import UserService
from src.service.UserServiceException import UserServiceException
from src.service.WorkoutService import WorkoutService
from src.util.ResponseUtil import ResponseUtil

class JMController:
    """
    Handles requests and responses to the user.
    """

    def __init__(self):
        self.firebase_db_client = FirebaseDBClient()
        self.auth = FirebaseAuthClient()
        self.user_service = UserService(self.firebase_db_client, self.auth)
        self.workout_service = WorkoutService(self.firebase_db_client)
        self.response_util = ResponseUtil()


    def get_user(self, id):
        result = self.user_service.load_user_by_id(id)
        logging.info("Successfully retrieved user:" + id)
        response = self.response_util.build_success_response(code=200, message="User Retrieved", data=result)
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


    def new_workout(self, data):

        try :
            workout_name = data['workout_name']
            category = data['category']
            is_repeated = data['is_repeated']
            date = data['date']
            userid = data['userid']
        except KeyError as e:
            message = "required field \'" + e.message + "\' not found"
            response = self.response_util.build_error_response(code=400, message=message)
            return response

        workout = self.workout_service.new_workout(
            userid=userid,
            name=workout_name,
            category=category,
            is_repeated=is_repeated,
            date=date
        )

        response = self.response_util.build_success_response(code=201, message='Workout Created', data=workout.toJSON())
        return response


    def add_exercise(self, data):

        try :
            exercise_name = data['exercise_name']
            weight = data['weight']
            rest_time = data['rest_time']
            total_sets = data['total_sets']
            total_reps = data['total_reps']
            userid = data['userid']
            workoutid = data['workoutid']
        except KeyError as e:
            message = "required field \'" + e.message + "\' not found"
            response = self.response_util.build_error_response(code=400, message=message)
            return response

        exercise = Exercise(
            name=exercise_name,
            weight=weight,
            rest_time=rest_time,
            total_sets=total_sets,
            total_reps=total_reps,
        )

        self.workout_service.save_workout(userid, workoutid, exercise)

        response = self.response_util.build_success_response(code=201, message='Exercise added', data=exercise.toJSON())
        return response


