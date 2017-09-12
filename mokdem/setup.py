from .tests import AuthTests, ProjectsTests


class Setup():
    def __init__(self, app):
        self.app = app
        auth = AuthTests(app, login='mok',
                         password='toto',
                         email='mok@mok.com')
        projects = ProjectsTests(app)
        auth.register()
        auth.log_in()
        projects.createProject("Setup Project 1")
        projects.createProject("Setup Project 2")
