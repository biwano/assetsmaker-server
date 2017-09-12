class AuthTests():
    def __init__(self, app, login, password, email):
        self.app = app
        self.login = login
        self.password = password
        self.email = email
        self.auth_tkt = None


    def log(self, info):
        print("setup: " + info)

    


    def register(self):
        self.log('register')
        params = {'login': self.login,
                  'password': self.password,
                  'email': self.email}
        response = self.app.post_json('/api/auth/register', params=params)
        assert response.json['status'] == 'ok', "register failed"

    def authinfo(self):
        self.log('authinfo')
        response = self.app.get('/api/auth/info')
        assert response.json['login'] == self.login, "get auth info failed"

    def log_out(self):
        self.log('logout')
        response = self.app.delete('/api/auth/info')
        assert response.json['status'] == 'ok', "logout failed"

    def log_in(self):
        self.log('login')
        params = {'login': self.login,
                  'password': self.password,
                  }
        response = self.app.post_json('/api/auth/info', params=params)
        assert response.json['login'] == self.login, "logout failed"

    def test(self):
        self.register()
        self.authinfo()
        self.log_out()
        self.log_in()
