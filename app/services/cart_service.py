from app.models.models import Cart
from app.services.abstract_service import AbstractService
from app.repos.cart_repo import CartRepository
from app.services.product_service import ProductService
from app.services.user_service import UserService



class CartService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return CartRepository()
    
    def create_cart(self, user_name, product_name):

        user = UserService().get_user_by_name(user_name)
        product = ProductService().get_product_by_name(product_name)

        if not user or not product:
            raise Exception('User or Product not found')
        
        
        cart = self.repository().find_by_user_id(user.id)

        if not cart:
            cart = Cart(user_id=user.id)
            cart = self.repository().save(cart)
            cart_item = self.repository().create_cart_item(cart.id, product.id, 1)
        else:
            cart_item = self.repository().create_cart_item(cart["id"], product.id, 1)

        return cart_item
    
    def get_by_user_id(self, user_id):
        return self.repository().find_by_user_id(user_id)
    
    def get_cart_by_user_name(self, user_name):
        user = UserService().get_user_by_name(user_name)
        if not user:
            raise Exception('User not found')

        return self.repository().find_by_user_id(user.id)

    def get_all(self):
        return self.repository().find_all()

    def get_by_id(self, id):
        return self.repository().find_by_id(id)
    
    def delete_by_id(self, id):
        return self.repository().delete_by_id(id)

