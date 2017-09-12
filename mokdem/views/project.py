from sqlalchemy import and_
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

        acl = Acl.create(self.request.user, project, Acl.Role.owner)
        self.db.merge(acl)

        return {"status": "ok",
                "project": to_dict(project)}

    @view_config(route_name="project_list", decorator=authenticated_view)
    def list_projects(self):
        projects = self.db.query(Project).filter(and_(Acl.user_id == self.request.user.id,
                                      Acl.target_type == Acl.Target.Project,
                                      Acl.target_id == Project.id)).all()

        return to_dict(projects)

    @view_config(route_name="project_get", decorator=authenticated_view)
    def get_project(self):
        project_id = int(self.request.matchdict['id'])
        project = self.db.query(Project).filter(and_(Acl.user_id == self.request.user.id,
                                      Acl.target_type == Acl.Target.Project,
                                      Project.id == project_id)).first()

        return to_dict(project)
