from datetime import datetime

from flask import Blueprint, render_template, jsonify
from flask import request


blueprint = Blueprint('register', __name__,url_prefix='/auth/register', static_folder='../static')


@blueprint.route('/')
def planOrProduct():
    return render_template('auth/planOrChoice.html')


@blueprint.route('/preRegistration')
def preRegistration():
    option = request.args.get('option')
    if option == 'plan':
        return render_template('auth/configurePlan.html')
    return render_template('auth/configureProduct.html')


@blueprint.route('/initRegistration')
def initRegistration():
    option = request.args.get('option')
    if option == 'plan':
        plan = request.args.get('plan')
        return render_template('auth/initRegistration.html')
    return render_template('auth/configureProduct.html')

