from flask import Blueprint
from flask_restplus import Api

from {{cookiecutter.app_name}}.api.resources import ping_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/')

api = Api(
    blueprint,
    title='{{cookiecutter.project_name}}',
    version='1.0-dev',
    description='{{cookiecutter.project_description}}')

api.add_namespace(ping_namespace, path='ping')