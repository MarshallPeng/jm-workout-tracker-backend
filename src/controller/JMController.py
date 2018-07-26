from flask import Flask, jsonify
import logging

from src.client.FirebaseClient import FirebaseClient
from src.service.UserService import UserService
from src.service.WorkoutService import WorkoutService


class JMController:

    def __init__(self):
        self.firebase_client = FirebaseClient()
        self.user_service = UserService(self.firebase_client)
        self.workout_service = WorkoutService(self.firebase_client)



