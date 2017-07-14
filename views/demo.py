from flask import Blueprint
from flask import render_template

blueprint = Blueprint('demo', __name__,url_prefix='/auth/request/demo', static_folder='../static')


@blueprint.route('/')
def demoAuth():
    return render_template('auth/login.html')

