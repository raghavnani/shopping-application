from flask import request, Response
from flask import Blueprint
from app.services.order_service import OrderService
from app.utils.sa_encoder import AlchemyEncoder
import json



service = OrderService()
order_api = Blueprint('order_api', __name__)


@order_api.route('/api/order', methods=['POST'])
def create_order():
        try:
            user_name = request.json['user_name']
            order = service.create_order(user_name)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(order, cls=AlchemyEncoder) , status=200, content_type="application/json")


@order_api.route('/api/get_order_by_name', methods=['GET'])
def get_order_by_name():
    
        try:
            user_name = request.args.get('user_name')
            orders = service.get_order_by_name(user_name)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(orders, cls=AlchemyEncoder) , status=200, content_type="application/json")

