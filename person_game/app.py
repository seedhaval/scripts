from flask import Flask, jsonify, request
import json
import random
import sqlite3
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)
dbfl = '/storage/internal/data/actions.db'

def curdate():
    return int(datetime.now().strftime("%s"))/86400

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

@app.route('/')
def home():
    return 'Test succesful'

@app.route('/get_ui_data')
def get_ui_data():
    out = {}
    out['person'] = fetch_db_results( "select * from person", [] )
    out['action'] = fetch_db_results( "select * from action", [] )
    return jsonify( out )

@app.route('/get_all_person_data')
def get_all_person_data():
    out = defaultdict(list)
    qry = "select * from active_action"
    data = fetch_db_results( qry, () )
    for r in data:
        out[r[0]].append( [r[1],r[2]] )
    return jsonify( out )

@app.route('/update_act_data', methods=['POST'])
def update_act_data():
    qry = "update action_person_map set last_dt = ? where action_nm = ? and person_nm = ?"
    data = request.json
    exec_query( qry, [curdate(), data['act'], data['prsn']] )
    return jsonify( {'out': 'done'} )
    
@app.route('/add_prsn', methods=['POST'])
def add_prsn():
    nm = request.json['person']
    qry = "insert into person select ?"
    exec_query( qry, [nm] )
    qry = "insert into action_person_map select action_nm, ?, ? from action"
    exec_query( qry, [nm, curdate() - 10] )
    return jsonify( {'out': 'done'} )

@app.route('/del_prsn', methods=['POST'])
def del_prsn():
    nm = request.json['person']
    qry = "delete from person where person_nm = ?"
    exec_query( qry, [nm] )
    qry = "delete from action_person_map where person_nm = ?"
    exec_query( qry, [nm] )
    return jsonify( {'out': 'done'} )

@app.route('/add_actn', methods=['POST'])
def add_actn():
    data = request.json
    qry = "insert into action select ?, ?, ?, ?, ?"
    exec_query( qry, [data['new_nm'], data['threshold'], data['strt_hr'], data['end_hr'], data['btn_txt']] )
    qry = "insert into action_person_map select ?, person_nm, ?"
    exec_query( qry, [data['action_nm'], curdate() - 10] )
    return jsonify( {'out': 'done'} )

@app.route('/del_actn', methods=['POST'])
def del_actn():
    data = request.json
    qry = "delete from action where action_nm = ?"
    exec_query( qry, [data['action_nm']] )
    qry = "delete from action_person_map where action_nm = ?"
    exec_query( qry, [data['action_nm']] )
    return jsonify( {'out': 'done'} )

@app.route('/upd_actn', methods=['POST'])
def upd_actn():
    data = request.json
    qry = 'update action set action_nm=?, threshold=?, strt_hr=?, end_hr=?, btn_txt=? where action_nm=?'
    exec_query( qry, [data['new_nm'], data['threshold'], data['strt_hr'], data['end_hr'], data['btn_txt'], data['action_nm']] )
    qry = 'update action_person_map set action_nm=? where action_nm=?'
    if data['new_nm'] != data['action_nm']:
        exec_query( qry, [data['new_nm'], data['action_nm']] )
    return jsonify( {'out': 'done'} )

app.run( port=1257 )
