from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/test')
def form():
    return "hello world"
