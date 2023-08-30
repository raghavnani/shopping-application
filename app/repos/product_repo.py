
from app.models.models import Product
from app.repos.abstract_repo import AbstractRepository
from app import db

class ProductRepository(AbstractRepository):

    def entity(self):
        return Product