import os

from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_migrate import Migrate
#from flask_moment import Moment
#from flask_bootstrap import Bootstrap
#from flask_pagedown import PageDown
#from flask_socketio import SocketIO, emit
from flask import Flask, render_template
from . import settings, controllers, models

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app

def register_extensions(app):
        """Register Flask extensions."""
        db = SQLAlchemy(app)
        migrate = Migrate(app,db)
        # bcrypt = Bcrypt(app)
        # moment = Moment(app)
        # bootstrap = Bootstrap(app)
        # pagedown = PageDown(app)
#        socketio = SocketIO(app)
        # login_manager = LoginManager(app)
        # login_manager.login_view = 'login'
        # login_manager.login_message_category = 'info'
def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.auth.blueprint)
    app.register_blueprint(controllers.tutorial.blueprint)
    return None

def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return render_template('401.html'), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return None
