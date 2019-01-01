from flask_restplus import Namespace, Resource

ping_namespace = Namespace(
    'ping', description='Ping endpoint for checking service availability.')


@ping_namespace.route('')
class PingAPI(Resource):
    '''
    Ping endpoint.
    '''

    def get(self):
        return {'response': 'OK'}, 200
