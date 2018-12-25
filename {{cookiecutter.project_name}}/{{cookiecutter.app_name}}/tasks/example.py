from {{cookiecutter.app_name}}.extensions import celery


@celery.task
def example_task():
    return 'OK'