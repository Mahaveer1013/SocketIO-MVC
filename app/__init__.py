from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
#from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
db_path = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(db_path, 'database.db'))
db = SQLAlchemy(app)
socketio = SocketIO(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# def load_user(user_id):
#     # This function loads a user from the session based on user_id
#     return User.query.get(int(user_id))

from app.models import User  # Import your User model here

with app.app_context():
    db.create_all()
    print("Database Created")

from app import views  # Import views last to avoid circular import
