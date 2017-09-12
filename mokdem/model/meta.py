from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()
    request.add_finished_callback(cleanup)

    return session


def init_from_dict(cls, dictionary):
    instance = cls()
    for k, v in dictionary.items():
        setattr(instance, k, v)

    return instance


def to_dict(obj):
    if type(obj) == list:
        result = [to_dict(o) for o in obj]

    else:
        dict_obj = obj.__dict__
        result = {}
        for k, v in dict_obj.items():
            v = dict_obj[k]
            if (v.__class__.__name__ == 'InstanceState'):
                pass
            else:
                result[k] = v
    return result
