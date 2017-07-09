from .tests import AuthTests


class Setup():
    def __init__(self, app):
        self.app = app
        auth = AuthTests(app, login='mok',
                         password='toto',
                         email='mok@mok.com')
        auth.register()
        auth.log_in()
