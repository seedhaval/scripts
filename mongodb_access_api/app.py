from flask import Flask, jsonify, request, redirect
import json

app = Flask(__name__)


@app.route('/')
def root():
    return redirect('static/access_mongo.html')


if __name__ == '__main__':
    app.run(port=3535)
