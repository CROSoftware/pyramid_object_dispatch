# encoding: utf-8

from pyramid.response import Response
from collections import deque
from collections.abc import Iterable
from webob.exc import HTTPNotFound

'''
An implementation of web.dispatch.object for pyramid.
'''

class Context(object):
    '''
    A psuedo implementation of WebCore's context object to better emulate the
    usage of web.dispatch.object
    '''
    def __init__(self, request, response):
        self.request = request
        self.response = response


def add_controller(self, route_name, pattern, controller, dispatcher, **kw):
    '''

    :params route_name:
        Specify a route_name for this controller

    :param pattern
        The url pattern to match for this controller, any sub urls will be routed
        through this controller's attributes until a match is found or HTTPNotFound
        Will be thrown.

    :param controller
        A class or function that will act as the controller class

    Additional parameters will be passed to the internal 'config.add_route()' call.

    '''

    if pattern is None:
        pattern = ''
    if pattern.endswith('/'):
        pattern = pattern[:-1]

    dispatch = dispatcher

    def controllerInternalView(request):
        url = request.matchdict['controller_path']

        path = url.split('/')
        path = deque(path)
        response = Response()
        context = Context(request, response)

        for segment, handler, endpoint, *meta in dispatch(context, controller, path):
            if(endpoint and not callable(handler)):
                raise HTTPNotFound('No endpoint found.')
            if endpoint:
                view_output = handler(*path)
                if isinstance(view_output, str):
                    response.text = view_output
                elif isinstance(view_output, Iterable):
                    response.app_iter = view_output
                return response

        response.status_code = 404
        response.status = '404 Not Found'

        return response

    self.add_route(route_name, pattern + '/{controller_path:.*}', **kw)
    self.add_view(view=controllerInternalView, route_name=route_name)

def includeme(config):
    config.add_directive('add_controller', add_controller)
