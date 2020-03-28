from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskapp.config import Config
# from flask_admin import User
# from flaskapp.models import Admin


db = SQLAlchemy()

bcrypt = Bcrypt()   


login_manager = LoginManager()

login_manager.login_view = 'users.login' 

login_manager.login_message_category = 'info'

mail = Mail()

from flask_admin.contrib.sqla import ModelView

# admin = Admin()

# admin.add_view(ModelView(User, db.session))


def create_app(config_class=Config):
    app =  Flask(__name__)
    app.config.from_object(Config)
    from flaskapp.models import db

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # admin.init_app(app)
    
    # admin = Admin(app, name='myblog', template_mode='bootstrap3')
    

    from flaskapp.users.routes import users
    from flaskapp.posts.routes import posts
    from flaskapp.main.routes import main
    from flaskapp.erorr.handlers import errors
    # from flaskapp.admin.ruoutes import admin


    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    # app.register_blueprint(admin)


    return app

