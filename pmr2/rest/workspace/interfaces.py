import zope.interface


class IRestView(zope.interface.Interface):
    """
    Rest view interface
    """


class IJsonView(zope.interface.Interface):
    """
    Json View interface
    """


class IWorkspaceExtraUtil(zope.interface.Interface):
    """
    Interface for utilities that will return additional information
    that may be relevant to a workspace.
    """
