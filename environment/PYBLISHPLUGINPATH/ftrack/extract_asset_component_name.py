import pyblish.api


class BlacksmithFtrackExtractAssetComponentName(pyblish.api.InstancePlugin):
    """Setting the asset name for components."""

    order = pyblish.api.ExtractorOrder
    label = "Asset/Component Name"

    def process(self, instance):

        name = instance.context.data["ftrackTask"]["name"]
        name += "_" + instance.data["name"]
        instance.data["asset_name"] = name

        instance.data["component_name"] = "main"
