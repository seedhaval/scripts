from flask import Flask, jsonify, request
import json
import uland
import shutil
import atexit
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return jsonify( {'out': 'received for sid ' + data['sid']} )

@app.route('/runpy/<string:cmd>')
def runpy(cmd):
    p = Popen(f'python3 {cmd}.py', cwd='/home/dvs/sdcard/pydroid/', shell=True,stdout=PIPE,stderr=PIPE,encoding='utf-8')
    output, error = p.communicate()
    return jsonify( {'output': output, 'error': error, 'returncode': p.returncode} )

@app.route('/upload_file', methods=['POST'])
def upload_file():
    data = request.json
    sess = uland.ServerSession(data['sid'])
    shutil.copy(sess.fldr+data['src'],'/home/dvs/'+data['tgt'])
    return jsonify( {'out': 'file uploaded to server'} )

@app.route('/run_cmd', methods=['POST'])
def run_cmd():
    data = request.json
    sess = uland.ServerSession(data['sid'])
    p = Popen(data['cmd'], stdout=PIPE, stderr=PIPE, shell=True, cwd=sess.fldr, encoding='utf-8')
    output, error = p.communicate()
    return jsonify( {'output': output, 'error': error, 'returncode': p.returncode} )

app.run( port=1257 )
