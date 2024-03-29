from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

ROLES_ENUM = ('admin', 'user')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(*ROLES_ENUM, name='roles_enum', create_type=False), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)
    cart = db.relationship('Cart', backref='user', lazy=True, uselist=False)

    def __repr__(self):
        return '<User %r>' % self.name
    
    # create index for user name
    __table_args__ = (
        db.Index(
            'ix_user_name',
            'name',
            unique=True
        ),
    )

    


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name
    
    # create index for product name
    __table_args__ = (
        db.Index(
            'ix_product_name',
            'name',
            unique=True
        ),
    )


class CartItem(db.Model):
    __tablename__ = 'cart_item'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('product.id'), nullable=False)
    cart_id = db.Column(UUID(as_uuid=True), db.ForeignKey('cart.id', ondelete="CASCADE"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)



    def __repr__(self):
        return '<OrderItem %r>' % self.id



class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    cart_items = db.relationship('CartItem', backref='cart', lazy=True)
    
    def __repr__(self):
        return '<Cart %r>' % self.id

    
 

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Order %r>' % self.id

    


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('product.id'), nullable=False)
    order_id = db.Column(UUID(as_uuid=True), db.ForeignKey('order.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<OrderItem %r>' % self.id

 

