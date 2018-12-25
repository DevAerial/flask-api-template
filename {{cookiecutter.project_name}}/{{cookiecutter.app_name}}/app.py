from celery import Celery
from dynaconf import FlaskDynaconf
from flask import Flask

from {{cookiecutter.app_name}} import api, extensions
from {{cookiecutter.app_name}}.celery import init_celery 


def configure_app(app):
    '''
    Configure app settings.
    '''
    FlaskDynaconf(app)


def init_extensions(app):
    '''
    Initialize Flask extensions.
    '''
    extensions.mongo.init_app(app)


def register_blueprints(app):
    '''
    Register blueprints for app.
    '''
    app.register_blueprint(api.views.blueprint){% if cookiecutter.use_celery == 'yes' %}


def init_celery(app=None):
    '''
    Initialize Celery instance
    '''
    if app:
        extensions.celery.conf.update(app.config)
    else:
        extensions.celery.conf.broker_url = settings['CELERY_BROKER_URL']
        extensions.celery.conf.result_backend = settings['CELERY_RESULT_BACKEND']

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    extensions.celery.Task = ContextTask
    extensions.celery.finalize()
    return extensions.celery{% endif %}


def create_app():
    ''' 
    Create new Flask app instance.
    '''
    app = Flask('{{cookiecutter.app_name}}')
    configure_app(app)
    init_extensions(app)
    register_blueprints(app)
    init_celery(app)
    return app
