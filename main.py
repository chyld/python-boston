import sys
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return "<h1>hello world</h1>"

@app.route('/version', methods=['GET'])
def version():
  return sys.version

# last line of code
app.run(host='0.0.0.0', port=3333, debug=True)
