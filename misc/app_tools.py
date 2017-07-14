
from flask import Flask
from flask import render_template

from config import ProdConfig

from misc.init import redis, db, admin
from views import login, register, demo, landing, products
from models import PlanModel, ProductsModel, NormanModelView


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0], template_folder="../templates", static_folder='../static')
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    redis.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    admin.add_view(NormanModelView(PlanModel))
    admin.add_view(NormanModelView(ProductsModel))


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(demo.blueprint)
    app.register_blueprint(login.blueprint)
    app.register_blueprint(register.blueprint)
    app.register_blueprint(landing.blueprint)
    app.register_blueprint(products.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        app.logger.error('A {0} HTTPException occurred'.format(errcode))
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.logger.error('A {0} server occurred'.format(errcode))
        app.errorhandler(errcode)(render_error)
    return None


def register_commands(app):
    """Register Click commands."""
    pass
