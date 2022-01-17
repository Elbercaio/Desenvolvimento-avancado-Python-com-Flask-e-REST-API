from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///devs.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()


class Devs(base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)
    email = Column(String(255), index=True)

    def __repr__(self):
        return f'<Developer {self.name}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Habilities(base):
    __tablename__ = 'habilities'
    id = Column(Integer, primary_key=True)
    hability = Column(String(80))

    def __repr__(self):
        return f'<Hability {self.name}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Dev_Hability(base):
    __tablename__ = 'dev_hability'
    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey("devs.id"))
    dev = relationship("Devs")
    hability_id = Column(Integer, ForeignKey("habilities.id"))
    hability = relationship("Habilities")

    def __repr__(self):
        return f'<Hability {self.name}>'

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
