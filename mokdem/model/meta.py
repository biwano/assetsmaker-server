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


def init_from_json(cls, dictionary):
    instance = cls()
    for k, v in dictionary.items():
        setattr(instance, k, v)

    return instance
