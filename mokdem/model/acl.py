import enum
from sqlalchemy import Column, Integer, String, Index, Enum
from .meta import Base, init_from_dict


class Acl(Base):
    __tablename__ = 'acl'

    class Target(enum.Enum):
        Project = 1
        Asset = 2

    class Role(enum.Enum):
        owner = 1

    user_id = Column(Integer, primary_key=True)
    target_type = Column(Enum(Target), primary_key=True)
    target_id = Column(Integer, primary_key=True)
    role = Column(Enum(Role))

    def __repr__(self):
        return "<User(target='%s', login='%s', email='%s')>" % (
             self.target_type, self.target_id, self.user_id)

    @staticmethod
    def create(user, item, role):
        acl_dict = {'user_id': user.id,
                    'target_type': item.__class__.__name__,
                    'target_id': item.id,
                    'role': role
                    }
        return init_from_dict(Acl, acl_dict)


Index('acl_index', Acl.user_id)
