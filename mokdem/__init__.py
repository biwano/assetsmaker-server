from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from .model import db, Base
from .helpers import parse_setting


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    engine = engine_from_config(settings, prefix='sqlalchemy.config.')

    if (parse_setting(settings, 'sqlalchemy.drop')):
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_request_method(db, reify=True)

#    config.include('pyramid_jinja2')
    config.add_static_view('app', 'app', cache_max_age=3600)
    config.add_route('auth_register', 'api/auth/register', request_method='POST')
#    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
