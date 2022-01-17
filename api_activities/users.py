from flask import request
from flask_restful import Resource
from models import UsersModel
from authentication import auth


class User(Resource):
    def get(self, id):
        try:
            user = UsersModel.query.filter_by(id=id).first()
            response = {
                'name': user.name,
                'age': user.age,
                'id': user.id
            }
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}
        return response

    @auth.login_required
    def put(self, id):
        try:
            user = UsersModel.query.filter_by(id=id).first()
            data = request.json
            if 'name' in data:
                user.name = data['name']
            if 'age' in data:
                user.age = data['age']
            user.save()
            response = {
                'name': user.name,
                'age': user.age,
                'id': user.id
            }
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}

        return response

    @auth.login_required
    def delete(self, id):
        try:
            user = UsersModel.query.filter_by(id=id).first()
            user.delete()
            response = {"statuscode": 200,
                        "message": "User successfully deleted"}
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}

        return response


class Users(Resource):
    def get(self):
        users = UsersModel.query.all()
        response = [{
            'name': user.name,
            'age': user.age,
            'id': user.id
        } for user in users]

        return response

    @auth.login_required
    def post(self):
        data = request.json
        user = UsersModel(name=data["name"], age=data["age"])
        user.save()
        response = {
            'name': user.name,
            'age': user.age,
            'id': user.id
        }
        return response
