from flask import Blueprint, render_template

blueprint = Blueprint('product', __name__, url_prefix='/products', static_folder='../static')


@blueprint.route('/', methods=['GET'])
def products():
    return render_template('index.html')


@blueprint.route('/bot', methods=['GET'])
def bot():
    return render_template('bot.html')


@blueprint.route('/analytics', methods=['GET'])
def analytics():
    return render_template('analytics.html')


@blueprint.route('/collate', methods=['GET'])
def collate():
    return render_template('collate.html')


@blueprint.route('/ipatient', methods=['GET'])
def ipatient():
    return render_template('patient.html')


@blueprint.route('/ihealth', methods=['GET'])
def ihealth():
    return render_template('health.html')


@blueprint.route('/idoctor', methods=['GET'])
def idoctor():
    return render_template('collate.html')
