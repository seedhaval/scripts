from flask import Flask, jsonify, request
import json
import random
import sqlite3

app = Flask(__name__)
dbfl = '/storage/internal/data/actions.db'

def fetch_db_results( qry, prm ):
    con = sqlite3.connect( dbfl )
    cur = con.cursor()
    cur.execute( qry, prm )
    ar = cur.fetchall()
    con.close()
    return ar

def exec_query( qry, prm ):
    con = sqlite3.connect( dbfl )
    cur = con.cursor()
    cur.execute( qry, prm )
    con.commit()
    con.close()

qry_ui_get = "select actions, property, restrictions, action_time_window, action_symbol, record_fmt, show from action_data"

qry_prsn_info = 'select actions, "%s" from action_data'

qry_updt = "update action_data set \"%s\" = '%s' where actions = '%s'"

@app.route('/')
def home():
    return 'Test succesful'

@app.route('/get_ui_data')
def get_ui_data():
    return jsonify( {'out': fetch_db_results( qry_ui_get, [] ) } )

@app.route('/get_person_data/<string:prsn>')
def get_person_data( prsn ):
    return jsonify( {'out': fetch_db_results( qry_prsn_info % (prsn), [] ) } )

@app.route('/update_act_data', methods=['POST'])
def update_act_data():
    data = request.json
    exec_query( qry_updt % (data['prsn'],data['newval'],data['act']), [] )
    return jsonify( {'out': 'done'} )
    

app.run( port=1257 )
