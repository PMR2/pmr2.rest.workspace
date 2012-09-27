import unittest
import doctest

from Testing import ZopeTestCase as ztc

from pmr2.app.workspace.tests import base

def test_suite():
    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'README.txt', package='pmr2.rest.workspace',
            test_class=base.WorkspaceDocTestCase,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
        ),

    ])
