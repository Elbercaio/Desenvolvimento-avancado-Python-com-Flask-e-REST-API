from flask import request
from flask_restful import Resource
import json
from habilities import habilities_list

developer_list = [{'id': 0,
                   'name': 'Elber',
                   'habilities': ['Python', 'Flask']},
                  {'id': 1,
                      'name': 'Rafael',
                   'habilities': ['Python', 'Django']}]


class Developer(Resource):
    def get(self, id):
        try:
            response = developer_list[id]
        except IndexError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}
        except Exception as e:
            response = {"statuscode": 400,
                        "message": e}
        return response

    def put(self, id):
        developer_list[id] = json.loads(request.data)
        response = developer_list[id]
        return response

    def delete(self, id):
        developer_list.pop(id)
        for i, dev in enumerate(developer_list):
            dev['id'] = i
        response = developer_list
        return response


class Developers(Resource):
    def get(self):
        response = developer_list
        return response

    def post(self):
        dev = json.loads(request.data)
        habilities = dev['habilities']
        for hability in habilities:
            if hability not in habilities_list:
                response = {"statuscode": 400,
                            "message": "Hability does not exist"}
                return response
        last_id = len(developer_list)
        dev.update({'id': last_id})
        developer_list.append(dev)
        response = developer_list[-1]
        return response
