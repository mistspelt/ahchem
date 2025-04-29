from flask import Blueprint, current_app
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import current_user
from app.models import oAuth
from app import db
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage

bp = Blueprint('auth', __name__)

from app.auth import oauth, routes