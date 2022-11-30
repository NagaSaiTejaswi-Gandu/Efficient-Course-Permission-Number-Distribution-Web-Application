import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def gert_current_tiem():
    return {'time': time.time()}