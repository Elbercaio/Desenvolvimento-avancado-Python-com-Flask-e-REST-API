from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///activities.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()


class UsersModel(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    def __repr__(self):
        return f'<User {self.name}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class ActivitiesModel(base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    activity = Column(String(80))
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_user = relationship("UsersModel")
    status = Column(String(10), default='pendente')

    def __repr__(self):
        return f'<Activitie {self.name}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
