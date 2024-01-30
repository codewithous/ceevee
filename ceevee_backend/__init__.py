from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def app_create():
    """ Create an app based on the configurations"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ceevee.db'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from ceevee_backend.users.routes import users

    app.register_blueprint(users)
    return app
