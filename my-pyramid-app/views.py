from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='myhelloRoute')
def hello_world(request):
    return Response('Hello!')