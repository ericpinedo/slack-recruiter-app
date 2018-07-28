from flask import Flask, jsonify, request
import httplib, urllib
import json
import requests
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    #r = requests.post(url='https://hooks.slack.com/services/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', data=json.dumps({'text':'Hello World'}))
    message = json.loads(request.data)
    try:
        print('inside try statement')
        print(message['event']['files'][0]['filetype'])

    except Exception:

        print('not a PDF')
    return request.data 

