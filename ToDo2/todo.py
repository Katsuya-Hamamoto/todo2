from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()  # Flask-Marshmallowの利用設定

def init_db(app):
  db.init_app(app)
  return db

def init_schema(app):  # Flask-Marshmallowオブジェクトをappオブジェクトで初期化
  ma.init_app(app)

class ToDoItem(db.Model):
  __tablename__ = "todoitems"
  item_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  done = db.Column(db.Boolean, nullable=False, default=False)

class ItemSchema(ma.Schema):
  class Meta:
    fields = ("item_id", "title", "done")

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
