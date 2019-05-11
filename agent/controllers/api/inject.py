from flask_restful import Resource
from agent.helpers.rest import * 
from ami.libs import inject
import os

class Inject(Resource):
    def get(self):
        # print(request.headers)
        return response(200, message="OK")

    def post(self):
        # data = request.body
        json = ""
        return response(200, message="OK")
