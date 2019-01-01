from celery import Celery
from dynaconf import FlaskDynaconf
from flask import Flask
from werkzeug.debug import DebuggedApplication

from {{cookiecutter.app_name}} import api, extensions
from {{cookiecutter.app_name}}.celery import init_celery 


def configure_app(app):
    '''
    Configure app settings.
    '''
    FlaskDynaconf(app)
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)


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
    app = app or create_app()
    extensions.celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    extensions.celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    extensions.celery.conf.update(app.config)

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
