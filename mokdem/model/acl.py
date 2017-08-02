from sqlalchemy import Column, Integer, String, Index
from .meta import Base, init_from_dict


class Acl(Base):
    __tablename__ = 'acl'

    user_id = Column(Integer, primary_key=True)
    target_type = Column(Integer, primary_key=True)
    target_id = Column(Integer, primary_key=True)

    TARGET_TYPE_PROJECT = 1
    TARGET_TYPE_ASSET = 1

    TARGET_NAME = {}
    TARGET_NAME[TARGET_TYPE_PROJECT] = 'Project'
    TARGET_NAME[TARGET_TYPE_ASSET] = 'Asset'

    def target_type_str(self):
        try:
            return TARGET_NAME[self.target_id]
        except Exception as e:
            return '?'

    def __repr__(self):
        return "<User(target='%s', login='%s', email='%s')>" % (
             TARGET_NAME[self.target_type], self.target_id, self.user_id)

    @staticmethod
    def create(user, item):
        acl_dict = {'user_id': user.id,
                    'target_type': item.__class__.__name__,
                    'target_id': item.id
                    }
        return init_from_dict(Acl, acl_dict)


Index('acl_index', Acl.user_id)
