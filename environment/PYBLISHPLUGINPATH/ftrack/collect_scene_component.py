import pyblish.api


class BlacksmithVFXFtrackCollectSceneComponent(pyblish.api.InstancePlugin):
    """ Appending data to scene instance """

    # offset to get instance from creation
    order = pyblish.api.CollectorOrder + 0.2
    families = ["scene"]
    label = "Scene"

    def process(self, instance):

        host = pyblish.api.current_host()

        # ftrack data
        if "ftrackComponents" in instance.data:

            components = instance.data["ftrackComponents"]
            data = {"path": instance.context.data["currentFile"],
                    "overwrite": True}
            components["%s_publish" % host] = data
            instance.data["ftrackComponents"] = components
