from pyramid.view import view_defaults, view_config
from pyramid.security import (
    remember,
    forget,
    )
from ..model import init_from_dict, to_dict, Project, Acl
from .view_helpers import authenticated_view
import bcrypt


@view_defaults(renderer='json')
class ProjectViews(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db


    @view_config(route_name="project_create", decorator=authenticated_view)
    def create_project(self):
        data = self.request.json_body

        project = Project()
        project.name = data['name']
        project = self.db.merge(project)
        self.db.flush()

        acl = Acl.create(self.request.user, project)
        self.db.merge(acl)

        return to_dict(project)
