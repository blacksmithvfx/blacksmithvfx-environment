import os
import tempfile

import hou

import pyblish.api
import ftrack
from ftrack_locations import ftrack_template_disk


class BlacksmithVFXHoudiniVersionUpScene(pyblish.api.Action):

    label = "Version Up"
    icon = "wrench"
    on = "all"

    def process(self, context, plugin):

        file_path = os.path.join(
            tempfile.gettempdir(), "pyblish-blacksmithvfx.hip"
        )
        hou.hipFile.save(file_name=file_path)

        task = ftrack.Task(context.data["ftrackData"]["Task"]["id"])

        asset = task.getParent().createAsset(
            task.getName(),
            "scene",
            task=task
        )

        location = ftrack_template_disk.get_old_location()
        components = asset.getVersions()[-1].getComponents(location=location)
        version = asset.createVersion(taskid=task.getId())

        # Recreating all components on new version
        for component in components:
            version.createComponent(
                name=component.getName(),
                path=component.getFilesystemPath(),
                location=location
            )

        asset.publish()
        path = version.getComponent(
            name=pyblish.api.current_host(), location=location
        ).getFilesystemPath()

        hou.hipFile.load(
            path,
            suppress_save_prompt=True,
            ignore_load_warnings=True
        )


class BlacksmithVFXHoudiniRepairScene(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):

        file_path = os.path.join(
            tempfile.gettempdir(), "pyblish-blacksmithvfx.hip"
        )
        hou.hipFile.save(file_name=file_path)

        ftrack_data = context.data["ftrackData"]
        task = ftrack.Task(ftrack_data["Task"]["id"])
        component_name = pyblish.api.current_host()
        location = ftrack_template_disk.get_old_location()

        asset = task.getParent().createAsset(
            task.getName(),
            "scene",
            task=task
        )

        version = None
        if asset.getVersions():
            version = asset.getVersions()[-1]
        else:
            version = asset.createVersion(taskid=task.getId())

        component = version.createComponent(
            name=component_name, path=file_path,
            location=location
        )
        component = location.getComponent(component.getId())

        asset.publish()

        hou.hipFile.load(
            component.getFilesystemPath(),
            suppress_save_prompt=True,
            ignore_load_warnings=True
        )


class BlacksmithVFXHoudiniValidateScene(pyblish.api.ContextPlugin):

    order = pyblish.api.ValidatorOrder
    label = "Scene"
    actions = [
        BlacksmithVFXHoudiniRepairScene, BlacksmithVFXHoudiniVersionUpScene
    ]
    hosts = ["houdini"]

    def process(self, context):

        ftrack_data = context.data["ftrackData"]
        task = ftrack.Task(ftrack_data["Task"]["id"])
        component_name = pyblish.api.current_host()
        location = ftrack_template_disk.get_old_location()

        assets = task.getAssets(
            assetTypes=["scene"],
            names=[ftrack_data["Task"]["name"]],
            componentNames=[component_name]
        )

        if not assets:
            raise ValueError("No existing Ftrack asset found.")

        component = assets[0].getVersions()[-1].getComponent(
            name=component_name
        )
        component = location.getComponent(component.getId())

        current = context.data["currentFile"].replace("\\", "/")
        current = current.replace("//", "/")
        expected = component.getFilesystemPath().replace("\\", "/")
        expected = expected.replace("//", "/")
        msg = "Scene path is not correct. Current: \"{0}\" Expected: \"{1}\""
        assert expected == current, msg.format(current, expected)
