from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblogapp.config import Config
from flask_ckeditor import CKEditor
from whitenoise import WhiteNoise
from flask_admin import Admin

db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail=Mail()
ckeditor = CKEditor()
admin = Admin()

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)
    admin.init_app(app, index_view=None, endpoint=None, url=None)

    from flaskblogapp.users.routes import users
    from flaskblogapp.posts.routes import posts
    from flaskblogapp.main.routes import main
    from flaskblogapp.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    app.wsgi_app = WhiteNoise(app.wsgi_app)

    my_static_folders = (
    'flaskblogapp/static/css/',
    'flaskblogapp/static/profile_pics'
    )

    return app
