from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

mail = Mail()

from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from app.models import oAuth

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    mail.init_app(app)

    # import and register blueprints
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp)

    from app.contact import bp as contact_bp
    app.register_blueprint(contact_bp)

    # create and register google oauth blueprint
    google_bp = make_google_blueprint(
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        scope=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"],
        storage=SQLAlchemyStorage(oAuth, db.session, user=current_user)
    )
    app.register_blueprint(google_bp, url_prefix="/login")

    return app

from app import models
