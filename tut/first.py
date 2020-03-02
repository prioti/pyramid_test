from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    config = Configurator()

    config.add_route('myhelloRoute', '/hello/')
    config.add_view(hello_world, route_name='myhelloRoute')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()