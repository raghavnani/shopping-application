from app.models.models import User
from app.services.abstract_service import AbstractService
from app.repos.user_repo import UserRepository


class UserService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return UserRepository()
    
    def create_user(self, name, email, role):
        user = User(name=name, email=email, role=role)
        return self.repository().save(user)
    
    def get_user_by_name(self, name):
        return self.repository().find_by_name(name)
