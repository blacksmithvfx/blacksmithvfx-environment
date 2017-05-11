import os

import pyblish.api
import nuke
import ftrack_template


class BlacksmithVFXNukeRepairScene(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):

        expected = BlacksmithVFXNukeValidateScene().get_expected_path(context)

        if os.path.exists(expected):
            msg = "\"{0}\" already exists. Please repair manually."
            raise ValueError(msg.format(expected))
        else:
            # Create parent directory if it doesn't exist
            if not os.path.exists(os.path.dirname(expected)):
                os.makedirs(os.path.dirname(expected))

            nuke.scriptSaveAs(expected)


class BlacksmithVFXNukeValidateScene(pyblish.api.ContextPlugin):

    order = pyblish.api.ValidatorOrder
    label = "Scene"
    actions = [BlacksmithVFXNukeRepairScene]
    hosts = ["nuke"]

    def process(self, context):

        # Get expected scene path
        expected = self.get_expected_path(context)

        # Get current scene path
        current = context.data["currentFile"]

        msg = "Scene path is failed. Current: \"{0}\". Expected: \"{1}\"."
        assert current == expected, msg.format(current, expected)

    def get_expected_path(self, context):

        task = context.data["ftrackTask"]
        templates = ftrack_template.discover_templates()
        padded_version = str(context.data.get("version", 1)).zfill(3)
        return ftrack_template.format(
            {"padded_version": padded_version, "nuke": "nuke"},
            templates,
            entity=task
        )[0]
