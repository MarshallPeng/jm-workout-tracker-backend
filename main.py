import logging
from flask import Flask, render_template, request

from src.controller.JMController import JMController

app = Flask(__name__)
controller = JMController()

@app.route('/test')
def form():
    return "hello dog"


@app.route('/register')
def register():
    logging.info("request received to register user: ")