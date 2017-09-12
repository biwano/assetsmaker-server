class ProjectsTests():
    def __init__(self, app):
        self.app = app

    def log(self, info):
        print("setup: " + info)

    def createProject(self, name):
        self.log('create')
        params = {'name': name
                  }
        response = self.app.post_json('/api/projects', params=params)
        assert response.json['status'] == 'ok', "register failed"
        return response.json["project"]
