import shutil
import threading
import subprocess
import os
import sys
import time
import datetime
import io
import re
import random
import base64
import uuid
import queue
import logging
import urllib.request
import traceback
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)
CORS(app)

#Queue for process OCR
ocr_queue = queue.Queue()
#Dict for result OCR
result_dict = dict()

def ocr_worker():
    while True:
        req = urllib.request.Request('http://localhost:{0}/'.format(port))
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print('from thread : http res => {0}'.format(body))      
        time.sleep(5.0)

ocr_thread = threading.Thread(target=ocr_worker)
ocr_thread.start()

@app.route('/')
def root_html():
    return 'ack'

@app.route('/ocr.js')
def root_js():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)),'ocr.js')

@app.route('/echo')
@cross_origin(origin='*')
def process_echo():
    return 'ack'

@app.route('/test')
@cross_origin(origin='*')
def test():
    cp = subprocess.run(['ls', '-1'], encoding='utf-8', stdout=subprocess.PIPE)
    return cp.stdout

@app.route('/test2')
@cross_origin(origin='*')
def test2():
    cp = subprocess.run(['ibmcloud'], encoding='utf-8', stdout=subprocess.PIPE)
    return cp.stdout

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)