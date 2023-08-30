from app.services.abstract_service import AbstractService
from app.repos.order_repo import OrderRepository
from app.services.user_service import UserService
from app.services.cart_service import CartService


class OrderService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return OrderRepository()
    
    def create_order(self, name):
        
        user = UserService().get_user_by_name(name)

        if user is None:
            raise Exception("User not found")

        cart = CartService().get_by_user_id(user.id)

        if cart is None:
            raise Exception("Cart not found")

        return self.repository().create_order(user, cart)

    def get_all(self):
        return self.repository().find_all()

    def get_by_id(self, id):
        return self.repository().find_by_id(id)
    
    def delete_by_id(self, id):
        return self.repository().delete_by_id(id)

