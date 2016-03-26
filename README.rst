=======================
Pyramid Object Dispatch
=======================

Introduction
============

Adds the functionality of an object based dispatcher to pyramid.


Installation
============
Currently there is no pip package available, instead you can clone and install the git version manually::

    git clone https://github.com/CROSoftware/pyramid_object_dispatch.git
    (cd pyramid_object_dispatch; python setup.py develop)

You can then upgrade to the latest version at any time::

    (cd pyramid_object_dispatch; git pull; python setup.py develop)


Usage
=====

Either include the framework to your Pyramid ini files::

    pyramid.includes =
        pyramid_debugtoolbar
        pyramid_object_dispatch

Or include it with Pyramid's Configurator located in `__init__.py` for scaffold projects::

    def main(global_config, **settings):
        ...
        config.include('pyramid_object_dispatch')

Next, you can add a controller via Pyramid's Configurator::

    class Controller:
        def __init__(self, context):
            #the context parameter contains the request and response objects
            self._ctx = context

        #This would be located at http://hostname:port/
        def __call__(self, _):
            return "Path: /"

        class Foo:
            def __init__(self, context):
                self._ctx = context

            def __call__(self, _):
                return "Path: /Foo"

            #Location: /Foo/bar/{name}
            def bar(self, name):
                return "Hello "+name

        #an example of the context object
        def chunked(self, _):
            self._ctx.response.app_iter = some_iterable()

    def main(global_config, **settings):
        ...
        config.add_controller('home', '/', Controller)

Framework Use
=============
Please see the web.dispatch.object framework at https://github.com/marrow/web.dispatch.object/
