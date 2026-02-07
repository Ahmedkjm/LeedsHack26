from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

# Used to create the database
db.create_all()