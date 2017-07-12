from flask import Blueprint, render_template
from flask import templating
# from security import norman_security

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@blueprint.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')


@blueprint.route('/pricing', methods=['GET'])
def pricing():
    return render_template('pricing.html')


@blueprint.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')


@blueprint.route('/hospital', methods=['GET'])
def hospital():
    return render_template('single-hospital.html')


@blueprint.route('/request-demo', methods=['GET'])
def demoRequest():
    return render_template('demo.html')


@blueprint.route('/features', methods=['GET'])
def features():
    return render_template('features.html')


@blueprint.route('/knowledge-base', methods=['GET'])
def knowledge():
    return render_template('knowledge.html')

