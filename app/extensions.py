"""Extensions module - Set up for additional libraries can go in here."""
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_migrate import Migrate
# from flask_moment import Moment
# from flask_bootstrap import Bootstrap
# from flask_pagedown import PageDown
#from flask_socketio import SocketIO, emit

db = SQLAlchemy()
migrate = Migrate(db)
# bcrypt = Bcrypt()
# moment = Moment()
# bootstrap = Bootstrap()
# pagedown = PageDown()
# socketio = SocketIO()
# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'