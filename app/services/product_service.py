from app.models.models import Product
from app.services.abstract_service import AbstractService
from app.repos.product_repo import ProductRepository


class ProductService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return ProductRepository()
    
    def create_product(self, name, price, quantity):
        product = Product(name=name, price=price, quantity=quantity)
        return self.repository().save(product)
    
    def get_product_by_name(self, name):
        return self.repository().find_by_name(name)
