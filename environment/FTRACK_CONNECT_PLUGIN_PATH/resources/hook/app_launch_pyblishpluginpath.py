import os
import logging

import ftrack


logging.basicConfig()
logger = logging.getLogger()


def appendPath(path, key, environment):
    """Append *path* to *key* in *environment*."""
    try:
        environment[key] = (
            os.pathsep.join([
                environment[key], path.replace("\\", "/")
            ])
        )
    except KeyError:
        environment[key] = path.replace("\\", "/")

    return environment


def modify_application_launch(event):
    """Modify the application launch command with potential files to open"""

    selection = event["data"]["context"]["selection"]

    if not selection:
        return

    environment = {}

    app_id = event["data"]["application"]["label"].lower()

    # Nukex = Nuke, no special plugins for NukeX
    if app_id == "nukex":
        app_id = "nuke"

    # Get task type
    task_type = ""
    try:
        task_id = event["data"]["context"]["selection"][0]["entityId"]
        task = ftrack.Task(task_id)
        task_type = task.getType().getName().lower()
    except:
        pass

    # PYBLISHPLUGINPATH
    bumpybox_plugins_dir = os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins"
    )
    environment_plugins_dir = os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "blacksmithvfx-environment",
        "environment",
        "PYBLISHPLUGINPATH"
    )
    environment["PYBLISHPLUGINPATH"] = [
        os.path.join(environment_plugins_dir, "deadline"),
        os.path.join(environment_plugins_dir, "ftrack"),
        os.path.join(environment_plugins_dir, "houdini"),
        os.path.join(environment_plugins_dir, "maya"),
        os.path.join(environment_plugins_dir, "nuke"),
        bumpybox_plugins_dir,
        os.path.join(bumpybox_plugins_dir, app_id.split("_")[0]),
        os.path.join(bumpybox_plugins_dir, app_id.split("_")[0], task_type),
        os.path.join(bumpybox_plugins_dir, "ftrack"),
        os.path.join(bumpybox_plugins_dir, "deadline"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-ftrack",
            "pyblish_ftrack",
            "plugins"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-deadline",
            "pyblish_deadline",
            "plugins"
        ),
    ]

    # adding variables
    data = event["data"]
    for variable in environment:
        for path in environment[variable]:
            appendPath(path, variable, data["options"]["env"])

    return data


def register(registry, **kw):
    """Register location plugin."""

    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    ftrack.EVENT_HUB.subscribe(
        "topic=ftrack.connect.application.launch",
        modify_application_launch
    )
