import os
import platform

import pyblish.api
import ftrack
import clique

from facility.structure import Structure


class CustomDiskAccessor(ftrack.DiskAccessor):

    def __init__(self, prefix, **kw):
        '''Initialise location accessor.

        *prefix* specifies the base folder for the disk based structure and
        will be prepended to any path. It should be specified in the syntax of
        the current OS.

        '''
        if prefix:
            prefix = os.path.expanduser(os.path.expandvars(prefix))
            prefix = os.path.abspath(prefix)
        self.prefix = prefix

        super(CustomDiskAccessor, self).__init__(prefix, **kw)

    def remove(self, resourceIdentifier):

        filesystemPath = self.getFilesystemPath(resourceIdentifier)

        if self.isFile(filesystemPath):

                os.remove(filesystemPath)

        elif self.isContainer(filesystemPath):

                os.rmdir(filesystemPath)

        sequence = self.getSequence(filesystemPath)
        if sequence:
            for item in sequence:
                os.remove(item)

    def getSequence(self, resourceIdentifier):
        filesystemPath = self.getFilesystemPath(resourceIdentifier)
        filesystemPath = filesystemPath.replace("\\", "/")
        root = os.path.dirname(filesystemPath)

        # return None if root path does not exist
        if not os.path.exists(root):
            return None

        items = []
        for item in os.listdir(root):
            items.append(os.path.join(root, item).replace("\\", "/"))

        collections = clique.assemble(items, minimum_items=1)[0]
        for col in collections:
            path = col.format('{head}{padding}{tail}').replace("\\", "/")
            if path == filesystemPath:
                return col

        return None

    def exists(self, resourceIdentifier):
        '''Return if *resourceIdentifier* is valid and exists in location.'''
        filesystemPath = self.getFilesystemPath(resourceIdentifier)

        if self.getSequence(filesystemPath):
            return True

        return os.path.exists(filesystemPath)


class DefaultStructure(Structure):
    def get_path_finder_args(self):
        default_path_finder_args = {
            'shot': {
                'task': {
                    'contain': ['shot_task'],
                    'ends': 'houdini'
                },
                'component': {
                    'contain': ['shot_task'],
                    'ends': '{asset_version}'
                }
            },
            'asset': {
                'task': {
                    'contain': ['asset_task'],
                    'ends': 'houdini'
                },
                'component': {
                    'contain': ['asset_task', 'asset_name'],
                    'ends': '{asset_version}'
                }
            }
        }
        return default_path_finder_args


class BlacksmithVFXFtrackIntegrateLocation(pyblish.api.InstancePlugin):
    """ Adds the Ftrack location name from the environment variables "SITE" and
    "STUDIO".
    """

    order = pyblish.api.IntegratorOrder + 0.39
    label = "Location"

    def process(self, instance):

        # skip if no components are present
        if "ftrackComponents" not in instance.data:
            return

        environment_location = os.environ["STUDIO"] + "." + os.environ["SITE"]
        location = ftrack.Location(environment_location)

        location.setStructure(DefaultStructure(location=environment_location))

        disk = ftrack.Disk(environment_location)
        if platform.system().lower() == "windows":
            location.setAccessor(CustomDiskAccessor(disk.get("windows")))
        else:
            location.setAccessor(CustomDiskAccessor(disk.get("unix")))

        components = instance.data["ftrackComponents"]
        for component_name in components:

            # special case to skip working scene file
            if "_work" in component_name:
                self.log.info("Skipping \"%s\"" % component_name)
                continue

            components[component_name]["location"] = location
