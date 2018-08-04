import logging
from flask import Flask, render_template, request

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.controller.JMController import JMController
from src.service.UserService import UserService

app = Flask(__name__)
controller = JMController()

@app.route('/test')
def form():
    return "hello dog"


@app.route('/register')
def register():
    logging.info("request received to register user: ")
    auth = FirebaseAuthClient()
    db = FirebaseDBClient()

    user_service = UserService(auth, db)
    user_service.initialize_user()

