from app import create_app, db
import sqlalchemy as sa
from app.models import User, Topic, Unit, Question

app = create_app()

