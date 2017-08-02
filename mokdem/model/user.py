from sqlalchemy import Column, Integer, String
from .meta import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return "<User(id='%s', login='%s', email='%s')>" % (
                             self.id, self.login, self.email)
