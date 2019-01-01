from enum import Enum

class ENVIRONMENT(Enum):
    DEVELOPMENT='development'
    PRODUCTION='production'
    STAGING='staging'

class MESSAGE(Enum):
    ERROR_404='Requested resource was not found.'
    ERROR_500='Internal server error.'