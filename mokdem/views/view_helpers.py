import venusian
from ..model import User


def authenticated_view(view_callable):
    def inner(context, request):
        user = request.db.query(User)\
            .filter(User.login == request.authenticated_userid).first()
        setattr(request, "user", user)
        return view_callable(context, request)

    return inner
