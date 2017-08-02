from pyramid.view import view_defaults, view_config
from pyramid.security import (
    remember,
    forget,
    )
from ..model import init_from_dict, User
import bcrypt


@view_defaults(renderer='json')
class AuthViews(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db

    def encrypt(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    @view_config(route_name="auth_register")
    def register(self):
        data = self.request.json_body
        checkuser = self.db.query(User)\
            .filter(User.login == data['login']
                    or User.email == data['email'])\
            .first()
        if (checkuser is not None):
            if (checkuser.login == data['login']):
                return {"status": "error_login_taken"}
            if (checkuser.email == data['email']):
                return {"status": "error_email_taken"}

        user = init_from_dict(User, data)
        user.password = self.encrypt(data['password'])
        self.db.merge(user)

        headers = remember(self.request, user.login)
        response = self.request.response
        response.headerlist.extend(headers)

        return {"status": "ok"}

    def infoBE(self, login):
        return dict(
            login=login
        )

    @view_config(route_name="auth_info")
    def info(self):
        return self.infoBE(self.request.authenticated_userid)

    @view_config(route_name="auth_logout")
    def logout(self):
        headers = forget(self.request)
        response = self.request.response
        response.headerlist.extend(headers)
        return {"status": "ok"}

    @view_config(route_name="auth_login")
    def login(self):
        data = self.request.json_body
        password = self.encrypt(data['password'])
        checkuser = self.db.query(User)\
            .filter(User.login == data['login']
                    and User.password == password)\
            .first()
        if (checkuser is not None):
            headers = remember(self.request, checkuser.login)
        else:
            headers = forget(self.request)
        response = self.request.response
        response.headerlist.extend(headers)

        return self.infoBE(checkuser.login)
