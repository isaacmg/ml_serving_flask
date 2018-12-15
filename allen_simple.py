from flask import Flask, request
from flask_restful import Resource, Api
import allennlp
from allennlp.predictors.predictor import Predictor
import json 

app = Flask(__name__)
api = Api(app)

class AllenWraper(Resource):
    def __init__(self):
        self.predictor = Predictor.from_path("url")
    def post(self):
        json.load(request.data)
        

api.add_resource(AllenWraper, '/get_model') 