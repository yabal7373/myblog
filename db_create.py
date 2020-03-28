from flaskapp import db
from flaskapp.models import User, Post

db.drop_all()

db.create_all()

db.session.commit()