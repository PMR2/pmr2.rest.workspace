import json

import zope.interface
from zope.publisher.browser import BrowserView

from pmr2.rest.workspace.interfaces import IJsonView


class BaseJsonView(BrowserView):
    """\
    Returns list of workspaces within the container.
    """

    zope.interface.implements(IJsonView)

    indent = 2
    # XXX if we are doing this, we need to make sure this only
    # return data that is NOT private
    origin = '*'

    def dumps(self, result):
        self.request.response.setHeader('Content-type', 'application/json')
        if self.origin:
            self.request.response.setHeader('Access-Control-Allow-Origin',
                self.origin)
        return json.dumps(result, indent=self.indent)


class BaseJsonEdit(BaseJsonView):
    """\
    Returns list of workspaces within the container.
    """

    origin = None
