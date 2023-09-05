
from app.models.models import Order, OrderItem, Cart, CartItem , Product
from app.repos.abstract_repo import AbstractRepository
from app import db

class OrderRepository(AbstractRepository):

    def entity(self):
        return Order
    
    def create_order(self, user, cart_dict):

        order = Order(user_id=user.id)
        cart = db.session.query(Cart).filter(Cart.id == cart_dict["id"]).first()
        

        order_price = 0
        for cart_item in cart_dict['cart_items']:

            order_price += cart_item["price_of_product"] * cart_item["quantity"]
            order_item = OrderItem(product_id=cart_item['product_id'], order_id=order.id, quantity=cart_item['quantity'], price=cart_item['price_of_product'] * cart_item['quantity'])
            order.order_items.append(order_item)

            product = db.session.query(Product).filter(Product.id == cart_item["product_id"]).first()
            product.quantity -= cart_item["quantity"]

            # delete cart item
            delete_cart_item = db.session.query(CartItem).filter(CartItem.id == cart_item['id']).first()
            db.session.delete(delete_cart_item)

        db.session.delete(cart)
        order.price = order_price
        db.session.add(order)
        db.session.commit()

        return order


    def get_order_by_name(self, user_id):        
        return db.session.query(Order).filter(Order.user_id == user_id).all()



            
