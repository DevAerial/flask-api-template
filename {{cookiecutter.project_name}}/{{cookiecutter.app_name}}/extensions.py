from flask_marshmallow import Marshmallow{% if cookiecutter.use_celery == 'yes'%}
from celery import Celery

celery = Celery(){% endif %}
ma = Marshmallow()

