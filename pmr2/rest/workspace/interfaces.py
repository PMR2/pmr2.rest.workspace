import zope.interface


class IJsonView(zope.interface.Interface):
    """
    Interface for utilities that will return additional information
    that may be relevant to a workspace.
    """


class IWorkspaceExtraUtil(zope.interface.Interface):
    """
    Interface for utilities that will return additional information
    that may be relevant to a workspace.
    """
