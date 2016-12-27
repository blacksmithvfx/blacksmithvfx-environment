import pyblish.api as api
from ftrack_locations import ftrack_template_disk


class BlacksmithVFXDeadlineOnJobFinishedCollectFtrack(api.InstancePlugin):
    """ Append Ftrack data """

    order = api.CollectorOrder + 0.1
    families = ["img", "cache", "render", "mov"]
    label = "Ftrack"

    def process(self, instance):

        instance.data["ftrackStatusUpdate"] = True

        families = instance.data["families"]
        asset_type = list(set(families) & set(self.families))[0]
        instance.data["ftrackAssetType"] = asset_type

        task_name = instance.context.data["ftrackData"]["Task"]["name"]
        instance.data["ftrackAssetName"] = task_name

        location = ftrack_template_disk.get_old_location()

        components = {}
        if len(instance.data["collections"]) == 1:
            data = {"path": instance.data["collections"][0].format(),
                    "overwrite": True, "location": location}
            components[instance.data["name"]] = data

        instance.data["ftrackComponents"] = components
