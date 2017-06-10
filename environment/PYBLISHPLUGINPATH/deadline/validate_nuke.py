import nuke

import pyblish.api


class BlacksmithDeadlineRepairParameters(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):

        # Get the errored instances
        failed = []
        for result in context.data["results"]:
            if (result["error"] is not None and
               result["instance"] is not None and
               result["instance"] not in failed):
                failed.append(result["instance"])

        # Apply pyblish.logic to get the instances for the plug-in.
        instances = pyblish.api.instances_by_plugin(failed, plugin)

        plugin = plugin()
        for instance in instances:

            node = instance[0]

            node["deadlinePool"].setValue("nuke")
            node["deadlinePriority"].setValue(90)
            node["deadlineLimits"].setValue("nuke")


class BlacksmithDeadlineValidateNukeParameters(pyblish.api.InstancePlugin):
    """ Validates the existence of deadline parameters on node. """

    order = pyblish.api.ValidatorOrder
    label = "Blacksmith Deadline Defaults"
    families = ["deadline"]
    hosts = ["nuke"]
    optional = True
    actions = [BlacksmithDeadlineRepairParameters]

    def process(self, instance):

        if "deadlinePool" in instance.data:
            msg = "Need a pool of \"nuke\". "
            msg += "Repair for default pool."
            assert instance.data["deadlinePool"] == "nuke", msg

        if "deadlinePriority" in instance.data:
            msg = "Need priority of 90. "
            msg += "Repair for default priority."
            assert instance.data["deadlinePriority"] == 90, msg

        if "deadlineLimits" in instance.data:
            msg = "Need limit of \"nuke\". "
            msg += "Repair for default limit."
            assert instance.data["deadlineLimits"] == "nuke", msg
