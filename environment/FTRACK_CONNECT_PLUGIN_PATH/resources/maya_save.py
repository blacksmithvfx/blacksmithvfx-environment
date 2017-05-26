import os

import ftrack_api
import ftrack_template

import maya.standalone

maya.standalone.initialize(name='python')

import pymel.core as pc


session = ftrack_api.Session()
task = session.get("Task", os.environ["FTRACK_TASKID"])
templates = ftrack_template.discover_templates()
path = ftrack_template.format(
    {"padded_version": "001", "maya": "maya"},
    templates,
    entity=task
)[0]

# Create parent directory if it doesn't exist
if not os.path.exists(os.path.dirname(path)):
    os.makedirs(os.path.dirname(path))

pc.system.saveAs(path)
