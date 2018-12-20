from flask import Flask, request
from flask_restful import Resource, Api

import allennlp
from allennlp.predictors.predictor import Predictor
import json 
import os 
app = Flask(__name__)
api = Api(app)
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz")

class AllenWraper(Resource):
    def __init__(self, environ="test"):
        # TODO get environment from Docker 
        if environ == "test":
            os.environ["token"] = "testToken"
        self.token = os.environ["token"]

    def predict(self, user_string: str):
        return predictor(user_string) 
    
    def process_result(self, result_text: str):
        pass 
        
    def get(self):
        print(request)
        data = json.loads(request.data)
        if data["token"] == self.token:
            result = predictor.predict(data["text"]) 
            return json.dumps({"result":result})

api.add_resource(AllenWraper, '/get_model') 


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)

