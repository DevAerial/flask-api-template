from flask import Blueprint
from flask import current_app, jsonify
from flask_restplus import Api

from {{cookiecutter.app_name}}.lib.constants import MESSAGE, ENVIRONMENT
from {{cookiecutter.app_name}}.api.resources import ping_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title='{{cookiecutter.project_name}}',
    version='1.0-dev',
    description='{{cookiecutter.project_description}}')


# Error handlers
@blueprint.app_errorhandler(404)
def path_not_found(error):
    return jsonify({'message': MESSAGE.ERROR_404.value}), 404


@api.errorhandler
def default_error_handler(error):
    message = MESSAGE.ERROR_500.value
    if current_app.config.ENV == ENVIRONMENT.PRODUCTION.value:
        return {'message': message}, 500


api.add_namespace(ping_namespace, path='/ping')