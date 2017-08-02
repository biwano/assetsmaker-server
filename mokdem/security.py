from pyramid.security import Allow, Everyone, Authenticated


def groupfinder(userid, request):
    return []

class Root(object):
    __acl__ = [(Allow, Authenticated, 'authenticated')]

    def __init__(self, request):
        pass
