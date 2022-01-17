from flask import Flask
from flask_restful import Api
from developers import Developer, Developers
from habilities import Hability, Habilities
app = Flask(__name__)
api = Api(app)


api.add_resource(Developer, "/devs/<int:id>")
api.add_resource(Developers, "/devs/")
api.add_resource(Hability, "/habilities/<int:id>")
api.add_resource(Habilities, "/habilities/")
