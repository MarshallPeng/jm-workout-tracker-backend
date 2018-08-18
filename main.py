import logging
from flask import Flask, render_template, request

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.controller.JMController import JMController
from src.service.UserService import UserService

app = Flask(__name__)
controller = JMController()
logging.basicConfig(level=logging.DEBUG)


@app.route('/test')
def form():
    return "hello dog"


@app.route('/users/<userid>', methods=['GET'])
def get_user(userid):

    logging.info("retrieving user " + userid)
    result = controller.get_user(userid)
    return result


@app.route('/register', methods=['POST'])
def register():
    logging.info("request to initialize user with data: " + str(request.json))
    result = controller.register(request.json)
    return result

@app.route('/workout', methods=['POST'])
def new_workout():
    logging.info("request to create new workout with data: " + str(request.json))
    result = controller.new_workout(request.json)
    return result

@app.route('/workout/<workoutid>/exercise', methods=['POST'])
def new_exercise(workoutid):
    logging.info("request to create new excercise with data: " + str(request.json))
    result = controller.add_exercise(request.json)
    return result


if __name__ == '__main__':
    app.run(debug=True)