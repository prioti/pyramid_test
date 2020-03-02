from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='myhelloRoute')
def hello_world(request):
    return Response('Hello!')


if __name__ == '__main__':
    config = Configurator()

    config.add_route('myhelloRoute', '/hello/')
    config.scan()

    # Создаём и запускаем приложение
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()