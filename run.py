from app import app
from app.routes.user_api import user_api
from app.routes.product_api import product_api
from app.routes.order_api import order_api
from app.routes.cart_api import cart_api


if __name__ == '__main__':

    # Register blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(product_api)
    app.register_blueprint(order_api)
    app.register_blueprint(cart_api)
    
    
    # Run the application
    app.run(host="0.0.0.0", debug=True, port=4000)
