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

    controller = JMController()
    logging.info("request to initialize user with data: " + str(request.json))
    result = controller.register(request.json)
    return result

@app.route('/workout', methods=['POST'])
def new_workout():
    controller = JMController()
    logging.info("request to create new workout with data: " + str(request.json))
    result = controller.new_workout(request.json)
    return result


if __name__ == '__main__':
    app.run(debug=True)