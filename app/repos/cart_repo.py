
from app.models.models import Cart, CartItem
from app.repos.abstract_repo import AbstractRepository
from app import db

class CartRepository(AbstractRepository):

    def entity(self):
        return Cart
    
    def create_cart_item(self, cart_id, product_id, quantity):

        # if cart item already exists, increment quantity
        cart_item = db.session.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.product_id == product_id).first()

        if cart_item:
            cart_item.quantity += quantity
            return self.save(cart_item)
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
            return self.save(cart_item)
        
    def find_by_user_id(self, user_id):
        return db.session.query(Cart).filter(Cart.user_id == user_id).first()