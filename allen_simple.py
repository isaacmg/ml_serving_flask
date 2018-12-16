from flask import Flask, request
from flask_restful import Resource, Api

import allennlp
from allennlp.predictors.predictor import Predictor
import json 
import os 
app = Flask(__name__)
api = Api(app)

class AllenWraper(Resource):
    def __init__(self, url=""):
        self.predictor = Predictor.from_path(url)
        self.token = os.environ["token"]

        
    def predict(self, user_string: str):
        return self.predictor(user_string) 
    
    def process_result(self, result_text):
        pass 
        
    def get(self):
        data = json.load(request.data)
        if data["token"] == self.token:
            result = self.predict(data["text"]) 
            return result 

api.add_resource(AllenWraper, '/get_model') 


if __name__ == '__main__':
    app.run(debug=True, port=5050, threaded=True)

