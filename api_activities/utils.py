from models import Users


def insert_user():
    user = Users(name='Galleani', age=25)
    user.save()


def select_user():
    users = Users.query.all()
    # user = Users.query.filter_by(name='Galleani').first()
    print(users)


def update_user():
    user = Users.query.filter_by(name='Galleani').first()
    user.name = 'Felipe'
    user.save()


def delete_user():
    user = Users.query.filter_by(name='Felipe').first()
    user.delete()


if __name__ == '__main__':
    insert_user()
    select_user()
    update_user()
    select_user()
    delete_user()
    select_user()
