=====================================
Web service access for PMR2 Workspace
=====================================

This module provides a web service access for PMR2 workspace.  To test
this out, we need to import required classes and set up some data.
::

    >>> from pmr2.app.workspace.content import *
    >>> self.portal['workspace'] = WorkspaceContainer()
    >>> self.portal.workspace.reindexObject()
    >>> self.portal.workspace['test1'] = Workspace('test1')
    >>> self.portal.workspace.test1.title = 'Test Dummy 1'
    >>> self.portal.workspace.test1.storage = u'dummy_storage'
    >>> self.portal.workspace.test1.reindexObject()
    >>> self.portal.workspace['test2'] = Workspace('test2')
    >>> self.portal.workspace.test2.title = 'Test Dummy 2'
    >>> self.portal.workspace.test2.storage = u'dummy_storage'
    >>> self.portal.workspace.test2.reindexObject()
    >>> from pmr2.testing.base import TestRequest
    >>> request = TestRequest()
    >>> from pmr2.rest.workspace import base
    >>> from pmr2.rest.workspace import page
    >>> from pmr2.rest.workspace import view
    >>> base.JsonGetView.indent = 4

We will test the workspace listing list and see that the request will 
return the list in JSON format.
::

    >>> v = view.WorkspaceContainerRestView(self.portal.workspace, request)
    >>> p = page.WorkspaceContainerContents(v, request)
    >>> result = p.render()
    >>> print result
    {
        "keys": [
            "Title",
            "URI"
        ],
        "values": [
            [
                "Test Dummy 1",
                "http://nohost/plone/workspace/test1"
            ],
            [
                "Test Dummy 2",
                "http://nohost/plone/workspace/test2"
            ]
        ]
    }

Do the same with one of the workspace
::

    >>> v = view.WorkspaceRestView(self.portal.workspace.test1, request)
    >>> p = page.WorkspaceInfo(v, request)
    >>> result = p.render()
    >>> print result
    {
        "storage": "dummy_storage",
        "description": null,
        "title": "Test Dummy 1"
    }
