import os, sys, shutil

use_celery = '{{cookiecutter.use_celery}}'

if use_celery == 'no':
    project_path = os.getcwd()
    app_path = os.path.join(
        project_path,
        '{{cookiecutter.app_name}}'
    )
    celery_tasks_path = os.path.join(app_path, 'tasks')
    celery_module_path = os.path.join(app_path, 'celery.py')
    try:
        os.remove(celery_module_path)
    except Exception as e:
        print(e)
        sys.exit(1)
    try:
        shutil.rmtree(celery_tasks_path)
    except Exception as e:
        print(e)
        sys.exit(1)