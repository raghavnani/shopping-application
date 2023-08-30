from flask import request, Response
from flask import Blueprint
from app.services.product_service import ProductService
from app.utils.sa_encoder import AlchemyEncoder
import json



service = ProductService()
product_api = Blueprint('product_api', __name__)


@product_api.route('/api/products', methods=['POST'])
def create_product():

        try:
            name = request.json['name']
            price = request.json['price']
            quantity = request.json['quantity']

            product = service.create_product(name, price, quantity)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(product, cls=AlchemyEncoder) , status=200, content_type="application/json")


@product_api.route('/api/products', methods=['GET'])
def get_all():
    
        try:
            products = service.get_all()
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(products, cls=AlchemyEncoder) , status=200, content_type="application/json")

@product_api.route('/api/products/<id>', methods=['GET'])
def get_by_id(id):
            try:
                product = service.get_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(product, cls=AlchemyEncoder) , status=200, content_type="application/json")

@product_api.route('/api/products/<id>', methods=['DELETE'])
def delete_by_id(id):
            try:
                product = service.delete_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

            return Response(json.dumps(product, cls=AlchemyEncoder) , status=200, content_type="application/json")


@product_api.route('/api/products/<id>', methods=['PUT'])
def update_by_id(id):
            try:
                product = service.update_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(product, cls=AlchemyEncoder) , status=200, content_type="application/json")
