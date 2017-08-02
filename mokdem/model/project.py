from sqlalchemy import Column, Integer, String
from .meta import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)

    def __repr__(self):
        return "<Project(id='%s', name='%s')>" % (
                             self.id, self.name)
