import json

from zope.publisher.browser import BrowserView


class BaseJsonView(BrowserView):
    """\
    Returns list of workspaces within the container.
    """

    indent = 2

    def dumps(self, result):
        self.request.response.setHeader('Content-type', 'application/json')
        # XXX if we are doing this, we need to make sure this only
        # return data that is NOT private
        self.request.response.setHeader('Access-Control-Allow-Origin', '*')
        return json.dumps(result, indent=self.indent)
