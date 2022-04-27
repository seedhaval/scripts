from flask import Flask, jsonify, request
import json
import random
import sqlite3

app = Flask(__name__)
dbfl = '/storage/internal/data/actions.db'

action_cols = ["action_nm","typ","inc_rate","threshold","action_time_window","action_symbol"]

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

qry_ui_get = "select %s from action_data" % (','.join( action_cols ))

qry_prsn_info = 'select action_nm, "%s" from action_data'

qry_updt = "update action_data set \"%s\" = '%s' where action_nm = '%s'"

qry_add_user_alter = "alter table action_data add \"%s\" text"
qry_add_user_update = "update action_data set \"%s\" = '01/04/2022'"

qry_col_list = "pragma table_info(action_data)"

qry_del_user_rename = "alter table action_data rename to action_data_bkp"
qry_del_user_create = "create table action_data as select %s from action_data_bkp"
qry_del_user_drop = "drop table action_data_bkp"

qry_actn_add = "insert into action_data ( %s ) values ( %s )"
qry_actn_del = "delete from action_data where action_nm = ?"
qry_actn_updt = "update action_data set " + ','.join( [x+' = ?' for x in action_cols] ) + " where action_nm = ?"

@app.route('/')
def home():
    return 'Test succesful'

@app.route('/get_ui_data')
def get_ui_data():
    all_cols = [x[1] for x in fetch_db_results( qry_col_list, [] )]
    prsn = set(all_cols) - set(action_cols)
    return jsonify( {'out': fetch_db_results( qry_ui_get, [] ), 'prsn_list': list(prsn) } )

@app.route('/get_person_data/<string:prsn>')
def get_person_data( prsn ):
    return jsonify( {'out': fetch_db_results( qry_prsn_info % (prsn), [] ) } )

@app.route('/update_act_data', methods=['POST'])
def update_act_data():
    data = request.json
    exec_query( qry_updt % (data['prsn'],data['newval'],data['act']), [] )
    return jsonify( {'out': 'done'} )
    
@app.route('/add_prsn', methods=['POST'])
def add_prsn():
    nm = request.json['person']
    exec_query( qry_add_user_alter % (nm), [] )
    exec_query( qry_add_user_update % (nm), [] )
    return jsonify( {'out': 'done'} )

@app.route('/del_prsn', methods=['POST'])
def del_prsn():
    nm = request.json['person']
    cols = ','.join( ['"'+x[1]+'"' for x in fetch_db_results( qry_col_list, [] ) if x[1] != nm] )
    exec_query( qry_del_user_rename, [] )
    exec_query( qry_del_user_create % (cols), [] )
    exec_query( qry_del_user_drop, [] )
    return jsonify( {'out': 'done'} )

@app.route('/add_actn', methods=['POST'])
def add_actn():
    data = request.json
    prsn_cols = ['"'+x[1]+'"' for x in fetch_db_results( qry_col_list, [] ) if x[1] not in action_cols]

    colnm = [x for x in action_cols]
    colnm.extend( prsn_cols )
    val = data['values']
    val.extend( ['01/04/2022']*len(prsn_cols) )
    colprm = ['?']*(len(action_cols) + len(prsn_cols))
    exec_query( qry_actn_add % (','.join(colnm), ','.join(colprm)), val )
    return jsonify( {'out': 'done'} )

@app.route('/del_actn', methods=['POST'])
def del_actn():
    data = request.json
    exec_query( qry_actn_del, [data['nm']] )
    return jsonify( {'out': 'done'} )

@app.route('/upd_actn', methods=['POST'])
def upd_actn():
    data = request.json
    ar = data['values']
    ar.append( data['nm'] )
    exec_query( qry_actn_updt, ar )
    return jsonify( {'out': 'done'} )

app.run( port=1257 )
