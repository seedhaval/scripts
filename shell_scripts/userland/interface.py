from flask import Flask, jsonify, request
import json
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/runpy/<string:cmd>')
def runpy(cmd):
    p = Popen(f'python3 {cmd}.py', cwd='/sdcard/pydroid/', shell=True,stdout=PIPE,stderr=PIPE,encoding='utf-8')
    output, error = p.communicate()
    return jsonify( {'output': output, 'error': error, 'returncode': p.returncode} )


@app.route('/runsh/<string:cmd>')
def runsh(cmd):
    p = Popen(f'bash {cmd}.sh', cwd='/sdcard/pydroid/', shell=True,stdout=PIPE,stderr=PIPE,encoding='utf-8')
    output, error = p.communicate()
    return jsonify( {'output': output, 'error': error, 'returncode': p.returncode} )

app.run( port=1257 )
