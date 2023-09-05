from flask import request, Response
from flask import Blueprint
from app.services.user_service import UserService
from app.utils.sa_encoder import AlchemyEncoder
import json



service = UserService()
user_api = Blueprint('user_api', __name__)


@user_api.route('/api/users', methods=['POST'])
def create_user():

        try:
            name = request.json['name']
            email = request.json['email']
            role = request.json['role']
            user = service.create_user(name, email, role)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(user, cls=AlchemyEncoder) , status=200, content_type="application/json")


@user_api.route('/api/users', methods=['GET'])
def get_all():
    
        try:
            users = service.get_all()
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(users, cls=AlchemyEncoder) , status=200, content_type="application/json")

@user_api.route('/api/users/<id>', methods=['GET'])
def get_by_id(id):
            try:
                user = service.get_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(user, cls=AlchemyEncoder) , status=200, content_type="application/json")
