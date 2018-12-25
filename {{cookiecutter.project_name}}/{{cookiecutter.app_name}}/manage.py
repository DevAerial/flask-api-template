import click
from flask.cli import FlaskGroup

from {{cookiecutter.app_name}}.app import create_app

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    '''
    Main entry point.
    '''

