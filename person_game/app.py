from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Test succesful'

@app.route('/get_data')
def get_data():
    with open( '/home/dvs/data/actions.json', 'r' ) as f:
        return jsonify( json.load( f ) )

@app.route('/update_data',methods=["POST"])
def update_data():
    with open( '/home/dvs/data/actions.json', 'w' ) as f:
        f.write( json.dumps( request.get_json(force=True), indent=2, ensure_ascii=False ) )
    return jsonify( {'out':'done'} )
    
app.run( port=1257 )
