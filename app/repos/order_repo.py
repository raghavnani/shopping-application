
from app.models.models import Order, OrderItem, CartItem
from app.repos.abstract_repo import AbstractRepository
from app import db

class OrderRepository(AbstractRepository):

    def entity(self):
        return Order
    
    def create_order(self, user, cart):


        # calculate the price of cart loop through cart items and get the price of each product 
        # and add it to the total price and add this cart item to the order items
        # and delete the cart item from the cart
        order = Order(user_id=user.id, cart_id=cart.id)

        price = 0
        for cart_item in cart.cart_items:

            # get cart item from db
            cart_item = db.session.query(CartItem).filter(CartItem.id == cart_item.id).first()
            print('hihhih')
            print(cart_item)

            price += cart_item.product.price * cart_item.quantity
            order_item = OrderItem(product_id=cart_item.product_id, order_id=order.id, quantity=cart_item.quantity)
            order.order_items.append(order_item)
            cart.cart_items.remove(cart_item)

        order.price = price
        db.session.add(order)
        db.session.commit()


            
