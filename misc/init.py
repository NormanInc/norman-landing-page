from flask_redis import FlaskRedis
from flask_mongoengine import MongoEngine
from flask_admin import Admin

db = MongoEngine()
redis = FlaskRedis()
admin = Admin(name='NormanAuth', template_mode='bootstrap3')
