from dynaconf import settings

from {{cookiecutter.app_name}}.app import init_celery

app = init_celery()