import boto3
import json
import os
from flask import redirect
import datetime
import numpy as np

from flask import Flask, request, url_for, jsonify

def up(obj, key):
    s3.Object(key=key).put(Body=json.dumps(obj))

s3 = boto3.resource("s3").Bucket("detect-rel")


app = Flask(__name__, template_folder='./')

@app.route('/')
def hello_world():
    with open('./index.html', 'r') as reader:
        doc = reader.read()
    return doc

@app.route('/test')
@app.route('/test.html')
def run_test():
    with open('./test.html', 'r') as reader:
        doc = reader.read()
    return doc

@app.route('/test/data', methods=['POST'])
def collect():
    # print(request.form.get_json())
    d = request.form.to_dict()
    data = json.loads(list(d.keys())[0])
    rnd = np.random.randint(100)
    key = 'quiz/detect-quiz-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '-' + str(rnd)
    up(data, key)
    return 'Submitted. Thank you!'



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))