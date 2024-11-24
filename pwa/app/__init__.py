# __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'cf748e101eefb5f9b595ea0a678954b76822fc81f81c3cc2c660da7bd5058625'

    # Import the blueprints here inside the create_app function
    from .routes import routes
    from .auth import auth

    # Register the blueprints with the app
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app