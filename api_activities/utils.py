from models import UsersModel


def insert_user():
    user = UsersModel(name='Galleani', age=25)
    user.save()
    user = UsersModel(name='Rafaele', age=27)
    user.save()


def select_user():
    users = UsersModel.query.all()
    # user = UsersModel.query.filter_by(name='Galleani').first()
    print(users)


def update_user():
    user = UsersModel.query.filter_by(name='Galleani').first()
    user.name = 'Felipe'
    user.save()


def delete_user():
    user = UsersModel.query.filter_by(name='Felipe').first()
    user.delete()


if __name__ == '__main__':
    insert_user()
    # select_user()
    # update_user()
    # select_user()
    # delete_user()
    # select_user()
