from flask import Flask, jsonify, request, redirect
from pymongo import MongoClient
import json
from bson import json_util


app = Flask(__name__)
with open('config.json') as f:
    conf = json.load(f)

client = MongoClient(conf['mongo_url'])
db = client[conf['mongo_dbase']]
coll = db[conf['mongo_coll']]


@app.route('/')
def root():
    return redirect('static/access_mongo.html')


@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.json
    coll.insert_one(data['document'])
    return jsonify({"out": "done"})


@app.route('/read_data', methods=['POST'])
def read_data():
    data = request.json
    empid = data['empid']
    out = coll.find_one({"empid":empid})
    print(out)
    return json_util.dumps(out)


@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    empid = data['empid']
    upd_data = data['new_values']
    coll.update_one({"empid":empid},{ "$set": upd_data } )
    return jsonify({"out": "done"})


@app.route('/delete_data', methods=['POST'])
def delete_data():
    data = request.json
    empid = data['empid']
    out = coll.delete_one({"empid":empid})
    return jsonify({"out": "done"})


if __name__ == '__main__':
    app.run(host=conf['api_bind_ip'], port=conf['api_bind_port'])
