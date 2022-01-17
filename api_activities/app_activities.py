from flask import Flask
from flask_restful import Api
from users import User, Users
from activities import Activity, Activities, ActivitiesByName
app = Flask(__name__)
api = Api(app)


api.add_resource(User, "/users/<int:id>")
api.add_resource(Users, "/users/")
api.add_resource(Activity, "/activities/<int:id>")
api.add_resource(Activities, "/activities/")
api.add_resource(ActivitiesByName, "/activities/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
