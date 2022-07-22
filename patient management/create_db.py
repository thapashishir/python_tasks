  
from web_app import app,db
from models.model import *

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()


