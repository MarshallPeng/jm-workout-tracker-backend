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


@app.route('/register', methods=['POST'])
def register():
    logging.info("request received to register user: ")
    controller = JMController()

    result = controller.register(
        email = request.json['email'],
        first_name= request.json['first_name'],
        last_name= request.json['last_name'],
        phone_number= request.json['phone_number'],
        password= request.json['password']
    )

    return result




