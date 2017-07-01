from pyramid.view import view_defaults, view_config
from ..model import init_from_json, User


@view_defaults(renderer='json')
class AuthViews(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db

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

        user = init_from_json(User, data)
        self.db.merge(user)

        return {"status": "ok"}
