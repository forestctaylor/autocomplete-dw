import os 
import pandas as pd

from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

from .helpers import loadSearchSuggestionData, querySearchSuggestions

def create_app():
    ls = loadSearchSuggestionData()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/getSearchSuggestions', methods=['POST'])
    def getSearchSuggestions():
        searchString = request.data.decode('utf-8')
        res = jsonify(querySearchSuggestions(searchString, ls))
        return res

    return app