from models import UsersModel, AdminsModel


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


def select_admin():
    admins = AdminsModel.query.all()
    print(admins)


def insert_admin():
    user = AdminsModel(login='Elber', password='123')
    user.save()


if __name__ == '__main__':
    insert_user()
    insert_admin()
    select_admin()
    # select_user()
    # update_user()
    # select_user()
    # delete_user()
    # select_user()
