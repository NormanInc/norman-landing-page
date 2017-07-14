import datetime
from flask_admin.contrib.mongoengine import ModelView
from misc.init import db
from misc.utils import generate_id


class PlanModel(db.Document):
    name = db.StringField(required=True, max_length=200, min_length=3, unique=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    short_description = db.StringField(max_length=2000, min_length=3)
    plan_id = db.StringField(required=True, max_length=30, min_length=3, default=generate_id(45))
    features = db.ListField(db.StringField(max_length=2000))
    price = db.StringField(required=True, max_length=10, min_length=3)


class ProductsModel(db.Document):
    name = db.StringField(required=True, max_length=200, min_length=3, unique=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    description = db.StringField(max_length=2000, min_length=3)
    product_id = db.StringField(required=True, max_length=30, min_length=3)
    features = db.ListField(db.StringField(max_length=2000))
    price = db.StringField(required=True, max_length=10, min_length=3)


class NormanModelView(ModelView):
    def is_accessible(self):
        return True

