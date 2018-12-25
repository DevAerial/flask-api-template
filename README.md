# Cookiecutter for RESTful Flask API 
Boilerpate for creating REST application using [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
## Description
-------------------------
Template for Flask RESTful applications based and inspired by [cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful) template.

## Requirements
-------------------------

Prerequisites:
* Python 3.6
* [pipenv](https://pipenv.readthedocs.io/en/latest/)

Packages:
* [Dynaconf](https://dynaconf.readthedocs.io/en/latest/index.html)
* [Gunicorn](https://gunicorn.org/)
* [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)
* [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [marshmallow](https://marshmallow.readthedocs.io/)
* [Celery](http://docs.celeryproject.org/en/latest/index.html) (optional)

## Usage
--------------------------
Initialize project:
```bash
$ cookiecutter flask-api-template
```
Install dependencies for development:
```bash
$ pipenv install --dev
```
Run app:
```bash
$ pipenv run flask run
```
It is also possible to install project in editable mode:
```bash
$ pipenv install -e .
```
Which allows to use cli commands defined in `manage.py`.
```
$ pipenv run {your_app_name}

Usage: {your_app_name} [OPTIONS] COMMAND [ARGS]...

  Main entry point.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Runs a development server.
  shell   Runs a shell in the app context.
```

