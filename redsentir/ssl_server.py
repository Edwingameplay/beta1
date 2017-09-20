#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webbrowser
from threading import Timer

os.environ["DJANGO_SETTINGS_MODULE"] = "redsentir.settings"

import cherrypy
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler

import django
django.setup()


class DjangoApplication(object):
    HOST = "0.0.0.0"
    PORT = 443

    def mount_static(self, url, root):
        """
        :param url: Relative url
        :param root: Path to static files root
        """
        config = {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': root,
            'tools.expires.on': True,
            'tools.expires.secs': 86400
        }
        cherrypy.tree.mount(None, url, {'/': config})

    def open_browser(self):
        Timer(3, webbrowser.open, ("http://%s:%s" % (self.HOST, self.PORT),)).start()

    def run(self):
        cherrypy.config.update({
            'server.socket_host' : self.HOST,
            'server.socket_port' : self.PORT,
            'server.ssl_module': 'pyopenssl',
            'server.ssl_certificate' : settings.BASE_DIR+'/ssl/redsentir.crt',
            'server.ssl_private_key' : settings.BASE_DIR+'/ssl/redsentir.key',
            'engine.autoreload_on': False,
            'log.screen': True
        })
        self.mount_static(settings.STATIC_URL, settings.STATIC_ROOT)

        cherrypy.log("Inciando la Plataforma de la Red Sentir.")
        cherrypy.tree.graft(WSGIHandler())
        cherrypy.engine.start()

        #self.open_browser()

        cherrypy.engine.block()


if __name__ == "__main__":
    DjangoApplication().run()
