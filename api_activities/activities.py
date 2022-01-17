from flask import request
from flask_restful import Resource
from models import ActivitiesModel, UsersModel
from authentication import auth


class Activity(Resource):
    def get(self, id):
        try:
            activity = ActivitiesModel.query.filter_by(id=id).first()
            response = {
                'name': activity.activity_user.name,
                'activity': activity.activity,
                'status': activity.status,
                'id': activity.id
            }
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}
        return response

    @auth.login_required
    def put(self, id):
        try:
            activity = ActivitiesModel.query.filter_by(id=id).first()
            data = request.json
            if 'status' in data:
                activity.status = data['status']
            activity.save()
            response = {
                'name': activity.activity_user.name,
                'activity': activity.activity,
                'status': activity.status,
                'id': activity.id
            }
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}

        return response

    @auth.login_required
    def delete(self, id):
        try:
            activity = ActivitiesModel.query.filter_by(id=id).first()
            activity.delete()
            response = {"statuscode": 200,
                        "message": "Activity successfully deleted"}
        except AttributeError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}

        return response


class Activities(Resource):
    def get(self):
        activities = ActivitiesModel.query.all()
        response = [{
            'name': activity.activity_user.name,
            'activity': activity.activity,
            'status': activity.status,
            'id': activity.id
        } for activity in activities]

        return response

    @auth.login_required
    def post(self):
        data = request.json
        activity_user = UsersModel.query.filter_by(name=data["name"]).first()
        activity = ActivitiesModel(
            activity=data["activity"], activity_user=activity_user)
        activity.save()
        response = {
            'name': activity.activity_user.name,
            'activity': activity.activity,
            'status': activity.status,
            'id': activity.id
        }
        return response


class ActivitiesByName(Resource):

    @auth.login_required
    def get(self, name):
        activity_user = UsersModel.query.filter_by(name=name).first()
        activities = ActivitiesModel.query.filter_by(
            activity_user=activity_user)
        response = [{
            'name': activity.activity_user.name,
            'activity': activity.activity,
            'status': activity.status,
            'id': activity.id
        } for activity in activities]

        return response
