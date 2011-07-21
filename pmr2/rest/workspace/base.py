import json

import zope.interface
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.browser import BrowserView

from pmr2.rest.workspace.interfaces import IRestView
from pmr2.rest.workspace.interfaces import IJsonView


class RestView(BrowserView):
    """\
    The "container" for all the get views.
    """

    zope.interface.implements(IRestView, IPublishTraverse)


class JsonGetView(BrowserView):
    """\
    The Json Get view
    """

    indent = 2
    origin = '*'

    def update(self):
        pass

    def render(self):
        pass

    def dumps(self, result):
        self.request.response.setHeader('Content-type', 'application/json')
        if self.origin:
            self.request.response.setHeader('Access-Control-Allow-Origin',
                self.origin)
        return json.dumps(result, indent=self.indent)

    def __call__(self):
        self.update()
        return self.render()


class JsonPostView(JsonGetView):
    """\
    The Json Post view
    """

    origin = None
