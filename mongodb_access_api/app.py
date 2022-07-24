from flask import Flask, jsonify, request, redirect
import json

app = Flask(__name__)
with open('config.json') as f:
    conf = json.load(f)


@app.route('/')
def root():
    return redirect('static/access_mongo.html')


if __name__ == '__main__':
    app.run(host=conf['api_bind_ip'],port=conf['api_bind_port'])
