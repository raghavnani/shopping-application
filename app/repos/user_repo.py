
from app.models.models import User
from app.repos.abstract_repo import AbstractRepository
from app import db

class UserRepository(AbstractRepository):

    def entity(self):
        return User