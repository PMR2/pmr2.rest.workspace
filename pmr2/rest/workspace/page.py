import json

import zope.interface
from zope.publisher.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from pmr2.rest.workspace.interfaces import IJsonView
from pmr2.rest.workspace.interfaces import IWorkspaceExtraUtil
from pmr2.rest.workspace.base import JsonGetView


class WorkspaceContainerContents(JsonGetView):

    def render(self):
        # XXX figure out how to simplify this
        workspace = self.context.context
        catalog = getToolByName(workspace, 'portal_catalog')

        query = {
            'portal_type': 'Workspace',
            'path': [
                u'/'.join(workspace.getPhysicalPath()),
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


class WorkspaceInfo(JsonGetView):

    def render(self):
        keys = ['title', 'description', 'storage',]
        workspace = self.context.context
        title = workspace.title
        description = workspace.description
        storage = workspace.storage

        values = [title, description, storage,]

        for name, util in zope.component.getUtilitiesFor(IWorkspaceExtraUtil):
            key = name
            value = util(workspace)

            keys.append(key)
            values.append(value)

        result = dict(zip(keys, values))

        return self.dumps(result)
