from pmr2.rest.workspace.base import RestView


class WorkspaceContainerRestView(RestView):
    """\
    Returns list of workspaces within the container.
    """


class WorkspaceRestView(RestView):
    """\
    Need to figure out what to return, because if this is use for
    model development, the tool should clone the workspace.
    """
