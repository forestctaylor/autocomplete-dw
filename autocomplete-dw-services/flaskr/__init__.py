import pandas as pd

from flask import Flask, request, Response
from flask.json import jsonify
from flask_cors import CORS

def querySearchSuggestions(searchString):
    return {'suggestions': ['DUMMY', 'DUMMY']}

def create_app():
    #df = pd.read_csv('./resources/user-ct-test-collection-01.txt')

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/getSearchSuggestions', methods=['POST'])
    def getSearchSuggestions():
        searchString = request.data
        return jsonify(querySearchSuggestions(searchString))

    return app