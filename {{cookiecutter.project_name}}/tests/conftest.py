import pytest

from {{cookiecutter.app_name}}.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client

