from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Test succesful'

app.run( port=1257 )
