import os

import pyblish.api


class BlacksmithVFXHoudiniExtractDeadline(pyblish.api.InstancePlugin):
    """ Appending Deadline data to houdini farm instances """

    families = ["deadline"]
    order = pyblish.api.ExtractorOrder
    label = "Deadline"

    def process(self, instance):

        job_data = {}
        plugin_data = {}
        if "deadlineData" in instance.data:
            job_data.update(instance.data["deadlineData"].get("job", {}))
            plugin_data.update(instance.data["deadlineData"].get("plugin", {}))

        # setting job data
        name = os.path.basename(instance.context.data["currentFile"])
        name = os.path.splitext(name)[0]
        job_data["Name"] = name + " - " + instance.data["name"]
        job_data["Pool"] = "all"

        # setting data
        data = {"job": job_data, "plugin": plugin_data}
        instance.data["deadlineData"] = data
