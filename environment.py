import os

from conda_git_deployment import utils


root = os.path.dirname(__file__)
env = {}

# PYTHONPATH
env["PYTHONPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-maya"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "pythonpath"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-template"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-locations"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-nuke"),
]

# NUKE_PATH
env["NUKE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "nuke_path"
    ),
    os.path.join(root, "environment", "NUKE_PATH")
]

# HOUDINI_PATH
env["HOUDINI_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "houdini_path"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-houdini",
        "pyblish_houdini",
        "houdini_path"
    ),
    "&"
]

# FTRACK_TEMPLATES_PATH
paths = [os.path.join(root, "environment", "FTRACK_TEMPLATES_PATH")]

env["FTRACK_TEMPLATES_PATH"] = paths

# FTRACK_CONNECT_PLUGIN_PATH
env["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "djv_plugin"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "pipeline_plugins"
    ),
    os.path.join(root, "environment", "FTRACK_CONNECT_PLUGIN_PATH")
]

# FTRACK_LOCATION_PLUGIN_PATH
env["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(root, "environment", "FTRACK_LOCATION_PLUGIN_PATH"),
]

# FTRACK_EVENT_PLUGIN_PATH
env["FTRACK_EVENT_PLUGIN_PATH"] = [
    os.path.join(root, "environment", "FTRACK_EVENT_PLUGIN_PATH"),
]

# FTRACK_LOCATIONS_MODULE
env["FTRACK_LOCATIONS_MODULE"] = [
    os.environ.get("FTRACK_LOCATIONS_MODULE", "ftrack_template_disk")
]

utils.write_environment(env)
