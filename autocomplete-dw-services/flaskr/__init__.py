import pandas as pd

from flask import Flask, request, Response
from flask_cors import CORS

def querySearchSuggestions(searchString):
    return 'DUMMY'

def create_app():
    #df = pd.read_csv('./resources/user-ct-test-collection-01.txt')

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/getSearchSuggestions', methods=['POST'])
    def getSearchSuggestions():
        searchString = request.data
        return Response(querySearchSuggestions(searchString))

    return app