import os

from conda_git_deployment import utils


environment = {}

# FTRACK_TEMPLATES_PATH
path = os.path.join(
    os.path.join(
        os.path.join(os.path.dirname(__file__)), "environment",
        "FTRACK_TEMPLATES_PATH"
    ),
)

environment["FTRACK_TEMPLATES_PATH"] = path

# PYBLISHPLUGINPATH
path = (
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-blacksmithvfx",
        "pyblish_blacksmithvfx", "plugins", "maya"
    ) +
    os.pathsep +
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-blacksmithvfx",
        "pyblish_blacksmithvfx", "plugins", "houdini"
    ) +
    os.pathsep +
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-deadline",
        "pyblish_deadline", "plugins"
    ) +
    os.pathsep +
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
        "pyblish_bumpybox", "plugins", "deadline"
    )
)

environment["PYBLISHPLUGINPATH"] = path

utils.write_environment(environment)
