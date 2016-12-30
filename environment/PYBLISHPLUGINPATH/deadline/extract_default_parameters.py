import pyblish.api as api


class BlacksmithDeadlineExtractDefaultParameters(api.InstancePlugin):
    """ Extracts a default value for Pool.

    Negative offset to come before BumpyboxDeadlineExtractHoudini.
    """

    order = api.ExtractorOrder - 0.1
    label = "Default Parameters"
    families = ["deadline"]

    def process(self, instance):

        value = instance.data.get("deadlinePool", "all")

        if value == "":
            value = "all"

        instance.data["deadlinePool"] = value
