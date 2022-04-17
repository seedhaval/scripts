from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Test succesful'

@app.route('/get_data')
def get_data():
    with open( '/home/dvs/data/actions.json', 'r' ) as f:
        return jsonify( json.load( f ) )

app.run( port=1257 )
