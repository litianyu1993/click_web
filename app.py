from flask import Flask
from flask import request
# from flask_cors import CORS, cross_origin
# from flask import jsonify, Response
# #import numpy as np
# import json

# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# #
# # app = Flask(__name__)
# # cors = CORS(app, resources={r"/api/*": {"origins": "*.officeapps.live.com"}})

# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8')
#         return json.JSONEncoder.default(self, obj)


@app.route('/')
def hello_world():
    return 'Hello World!'

# es = []

# @app.route('/', methods=['POST', 'GET'])
# @cross_origin()
# def login():
#     if request.method == 'POST':
#         es.append(request.data)

#         return 'ok'
#     else:
#         json_es = json.dumps(es, cls=MyEncoder,indent=4)
#         return json_es
