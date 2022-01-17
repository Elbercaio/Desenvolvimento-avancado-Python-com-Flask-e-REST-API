
from flask_httpauth import HTTPBasicAuth
from models import AdminsModel

auth = HTTPBasicAuth()


@auth.verify_password
def authenticate(login, password):
    if not (login, password):
        return False
    print(AdminsModel.query.filter_by(login=login, password=password).first())
    return AdminsModel.query.filter_by(login=login, password=password).first()
