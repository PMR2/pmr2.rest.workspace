import zope.interface
import zope.component

from Products.CMFCore.utils import getToolByName

from pmr2.rest.workspace.interfaces import IWorkspaceExtraUtil
from pmr2.rest.workspace.base import BaseJsonView


class WorkspaceContainerJsonView(BaseJsonView):
    """\
    Returns list of workspaces within the container.
    """

    def contents(self):
        # XXX figure out how to simplify this
        catalog = getToolByName(self.context, 'portal_catalog')

        query = {
            'portal_type': 'Workspace',
            'path': [
                u'/'.join(self.context.getPhysicalPath()),
            ],
            'sort_on': 'sortable_title',
        }
        results = catalog(**query)

        keys = ['Title', 'URI']
        values = ([(i.Title, i.getURL(),) for i in results])
        result = {
            'keys': keys,
            'values': values,
        }
        return self.dumps(result)


class WorkspaceJsonView(BaseJsonView):
    """\
    Need to figure out what to return, because if this is use for
    model development, the tool should clone the workspace.
    """

    def info(self):
        keys = ['title', 'description', 'storage',]
        title = self.context.title
        description = self.context.description
        storage = self.context.storage

        values = [title, description, storage,]

        for name, util in zope.component.getUtilitiesFor(IWorkspaceExtraUtil):
            key = name
            value = util(self.context)

            keys.append(key)
            values.append(value)

        result = dict(zip(keys, values))

        return self.dumps(result)
