from flask import Flask, request
from flask_restful import Resource, Api

import allennlp
from allennlp.predictors.predictor import Predictor
import json 
import os 
app = Flask(__name__)
api = Api(app)

class AllenWraper(Resource):
   def __init__(self, url: str):
        self.predictor = Predictor.from_path(url)
        self.token = os.environ["token"]
        
    def predict(user_string: str):
        return self.predictor(user_string) 
        
    def post(self):
        data = json.load(request.data)
        if data["token"] == token:
            pass
        
        
        

api.add_resource(AllenWraper, '/get_model') 
