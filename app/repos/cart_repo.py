
from app.models.models import Cart, CartItem, Product
from app.repos.abstract_repo import AbstractRepository
from app import db

class CartRepository(AbstractRepository):

    def entity(self):
        return Cart
    
    def create_cart_item(self, cart_id, product_id, quantity):

        # if cart item already exists, increment quantity
        cart_item = db.session.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.product_id == product_id).first()

        # check if product quantity is available
        product = db.session.query(Product).filter(Product.id == product_id).first()
        if cart_item:
            if product.quantity < cart_item.quantity + quantity:
                raise Exception(f'Not enough quantity available for product {product.name}')
            cart_item.quantity += quantity
            return self.save(cart_item)
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
            return self.save(cart_item)
                
    def find_by_user_id(self, user_id):
        cart =  db.session.query(Cart).filter(Cart.user_id == user_id).first()

        # populate cart items and products for each cart
        if cart:
            return_cart = {
            "id": str(cart.id),
            'user_name' : cart.user.name,
            'total_cart_price' : 0,
            'cart_items' : []
            }

            for cart_item in cart.cart_items:

                product = db.session.query(Product).filter(Product.id == cart_item.product_id).first()

                return_cart_item = {
                    'id': str(cart_item.id),
                    'product_id': str(product.id),
                    'quantity': cart_item.quantity,
                    'product': product.name,
                    'price_of_product': product.price,
                    'total_price': product.price * cart_item.quantity
                }


                return_cart['total_cart_price'] += product.price * cart_item.quantity
                return_cart['cart_items'].append(return_cart_item)

            return return_cart
        else:
            return None


