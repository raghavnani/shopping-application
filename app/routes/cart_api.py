from flask import request, Response
from flask import Blueprint
from app.services.cart_service import CartService
from app.utils.sa_encoder import AlchemyEncoder
import json



service = CartService()
cart_api = Blueprint('cart_api', __name__)


@cart_api.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():

        try:
            user_name = request.json['user_name']
            product_name = request.json['product_name']            
            cart = service.create_cart(user_name, product_name)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(cart, cls=AlchemyEncoder) , status=200, content_type="application/json")


@cart_api.route('/api/cart', methods=['GET'])
def get_all():
    
        try:
            user_name = request.args.get('user_name')
            carts = service.get_cart_by_user_name(user_name)


        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(carts, cls=AlchemyEncoder) , status=200, content_type="application/json")
