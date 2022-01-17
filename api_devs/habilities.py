from flask import request
from flask_restful import Resource
import json

habilities_list = ['Flask', 'Django',
                   'python', 'redis', 'sql', 'php', 'Laravel']


class Hability(Resource):
    def get(self, id):
        try:
            response = habilities_list[id]
        except IndexError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}
        except Exception as e:
            response = {"statuscode": 400,
                        "message": e}
        return response

    def put(self, id):
        habilities_list[id] = json.loads(request.data)["hability"]
        response = habilities_list
        return response

    def delete(self, id):
        habilities_list.pop(id)
        response = habilities_list
        return response


class Habilities(Resource):
    def get(self):
        response = habilities_list
        return response

    def post(self):
        hability = json.loads(request.data)["hability"]
        habilities_list.append(hability)
        response = habilities_list[-1]
        return response
