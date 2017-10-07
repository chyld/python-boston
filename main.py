import sys
import json
from flask import Flask, render_template, request
from watson_developer_cloud import ToneAnalyzerV3
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return "<h1>hello world</h1>"

@app.route('/version', methods=['GET'])
def version():
  return sys.version

@app.route('/tone', methods=['GET'])
def get_tone():
  return render_template('tone.html')

@app.route('/tone', methods=['POST'])
def post_tone():
  u = '4b58fe22-63a1-41ae-97ed-e065addbf3b7'
  p = 'oDaVtVf3nHqo'
  v = '2016-05-19'
  text = request.values['tone']
  t = ToneAnalyzerV3(username=u, password=p, version=v)
  d = t.tone(text)
  from IPython import embed; embed()
  return render_template('tone.html')

# last line of code
app.run(host='0.0.0.0', port=3333, debug=True)



# {
#   "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
#   "username": "4b58fe22-63a1-41ae-97ed-e065addbf3b7",
#   "password": "oDaVtVf3nHqo"
# }
