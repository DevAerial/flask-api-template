#!/bin/bash

gunicorn --log-level=debug \
        --workers 4 --name {{cookiecutter.app_name}} \
        -b 0.0.0.0:8000 \
        --reload {{cookiecutter.app_name}}.wsgi:app \
        -t 100000