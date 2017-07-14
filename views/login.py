from flask import Blueprint, render_template
# from security import norman_security

blueprint = Blueprint('login', __name__,url_prefix='/auth/login', static_folder='../static')


@blueprint.route('/')
def loginAuth():
    return render_template('auth/login.html')



