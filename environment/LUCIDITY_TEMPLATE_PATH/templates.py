import os
import platform

import lucidity


class Template(lucidity.Template):

    def get_parents(self, entity, parents):
        """Recursive iterate to find all parents.
        For AssetVersion where no parent is present, the asset is assumed as
        parent.
        For SequenceComponent and FileComponent where no parent is present, the
        asset version is assumed as parent.
        """

        try:
            parent = entity["parent"]
            if parent:
                parents.append(parent)
                return self.get_parents(parent, parents)
        except KeyError:
            if entity.entity_type == "AssetVersion":
                parents.append(entity["asset"])
                return self.get_parents(entity["asset"], parents)

            if entity.entity_type == "FileComponent":

                parent = entity["version"]
                # Assuming its in a container, if there are no version.
                if parent:
                    parents.append(entity["version"])
                else:
                    parent = entity["container"]
                    parents.append(entity["container"])
                return self.get_parents(parent, parents)

            if entity.entity_type == "SequenceComponent":
                parents.append(entity["version"])
                return self.get_parents(entity["version"], parents)

        return parents

    def get_entity_type_path(self, entities):
        """Get the entity type path from a list of entities
        The returned path is a list of entity types separated by a path
        separator:
            "[entity_type]/[entity_type]/[entity_type]"
            "Project/Asset/AssetVersion"
        For further uniqueness the file_type data member (extension) is used
        for components. This results in paths like this:
            "Project/Asset/AssetVersion/FileComponent/[file_type]"
            "Project/Asset/AssetVersion/FileComponent/.txt"
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr
            /FileComponent/.exr"
        """

        entity_types = []
        for entity in entities:
            entity_types.append(entity.entity_type)

            try:
                entity_types.append(entity["file_type"])
            except KeyError:
                pass

        return "/".join(entity_types)

    def get_template_name(self, entity):
        """Convenience method for getting the template name
        The template name is generated from the entity's parents, and their
        entity type.
        """

        entities = list(reversed(self.get_parents(entity, [])))
        entities.append(entity)
        return self.get_entity_type_path(entities)

    def get_valid_templates(self, entity, templates):

        results = []
        template_name = self.get_template_name(entity)
        try:
            template_name = entity["metadata"]["lucidity_template_name"]
        except KeyError:
            pass

        for template in templates:
            if template.name == template_name:
                results.append(template)

        return results

    def format(self, data):

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "AssetVersion":
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "FileComponent":
            if data["version"]:
                version_string = str(data["version"]["version"]).zfill(3)
                data["version"]["version"] = version_string
            else:
                version_string = str(
                    data["container"]["version"]["version"]
                ).zfill(3)
                data["container"]["version"]["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "SequenceComponent":
            version_string = str(data["version"]["version"]).zfill(3)
            data["version"]["version"] = version_string

            # "padding" data member needs to be convert from integer to string.
            padding_string = str(data["padding"]).zfill(2)
            data["padding"] = padding_string

        if data.entity_type == "Task" and "version" in data.keys():
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        return os.path.abspath(
            super(Template, self).format(data)
        ).replace("\\", "/")


def register():
    '''Register templates.
    Templates are named according to the entity in the hierarchy,
    they aim to solve paths for.
    For example a template named "Project" is only for paths for the project.
    Nested entity types are specified with a path separator, for example
    "Project/Shot" deals with paths for shots under the project.
    To specify dealing with certain file types, the file types extension is
    added. For example a template named "Project/.nk" deals with Nuke script
    paths under the project.
    It is assumed that asset versions are children of the asset, resulting in a
    path "Project/Asset/AssetVersion".
    '''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    templates = []

    # project
    mount = "{disk." + system_name + "}/{root}/{name}"
    templates.extend([
        Template("Project", mount),
        Template("Project", mount + "/in/elements"),
        Template("Project", mount + "/in/footage/grade"),
        Template("Project", mount + "/in/footage/raw"),
        Template("Project", mount + "/in/roughCuts"),
        Template("Project", mount + "/in/references/fromClient"),
        Template("Project", mount + "/in/shoot/scriptNotes"),
        Template("Project", mount + "/in/shoot/stills"),
        Template("Project", mount + "/in/GFX"),
        Template("Project", mount + "/in/assets"),
        Template("Project", mount + "/in/EDL"),
        Template("Project", mount + "/in/production/storyboards"),
        Template("Project", mount + "/in/production/treatment"),
        Template("Project", mount + "/in/production/script"),
        Template("Project", mount + "/in/roto"),
        Template("Project", mount + "/in/audio"),
        Template("Project", mount + "/out/tracking"),
        Template("Project", mount + "/out/mattePainting"),
        Template("Project", mount + "/out/deliverables"),
        Template("Project", mount + "/out/client"),
        Template("Project", mount + "/out/cleanUp"),
        Template("Project", mount + "/out/roto"),
    ])

    # project/task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "Tasks/{name}"
    )
    templates.extend([
        Template("Project/Task", mount),
        Template("Project/Task", mount + "/Work/nuke/scripts"),
        Template(
            "Project/Task", mount + "/Work/maya/sourceimages/3dPaintTextures"
        ),
        Template("Project/Task", mount + "/Work/maya/autosave"),
        Template("Project/Task", mount + "/Work/maya/scripts"),
        Template("Project/Task", mount + "/Work/maya/images"),
        Template("Project/Task", mount + "/Work/maya/data"),
        Template("Project/Task", mount + "/Work/maya/sound"),
        Template("Project/Task", mount + "/Work/maya/particles"),
        Template("Project/Task", mount + "/Work/maya/assets"),
        Template("Project/Task", mount + "/Work/maya/cache/bifrost"),
        Template("Project/Task", mount + "/Work/maya/cache/particles"),
        Template("Project/Task", mount + "/Work/maya/cache/nCache"),
        Template("Project/Task", mount + "/Work/maya/cache/alembic"),
        Template("Project/Task", mount + "/Work/maya/scenes/edit"),
        Template("Project/Task", mount + "/Work/maya/clips"),
        Template("Project/Task", mount + "/Work/maya/movies"),
        Template("Project/Task", mount + "/Work/maya/renderData/iprImages"),
        Template("Project/Task", mount + "/Work/maya/renderData/depth"),
        Template("Project/Task", mount + "/Work/maya/renderData/fur/furFiles"),
        Template(
            "Project/Task", mount + "/Work/maya/renderData/fur/furImages"
        ),
        Template(
            "Project/Task", mount + "/Work/maya/renderData/fur/furShadowMap"
        ),
        Template(
            "Project/Task", mount + "/Work/maya/renderData/fur/furEqualMap"
        ),
        Template(
            "Project/Task", mount + "/Work/maya/renderData/fur/furAttrMap"
        ),
        Template("Project/Task", mount + "/Work/flame"),
        Template("Project/Task", mount + "/Work/houdini/hip"),
        Template("Project/Task", mount + "/Work/houdini/tex"),
        Template("Project/Task", mount + "/Work/houdini/geo"),
        Template("Project/Task", mount + "/Work/houdini/sim"),
        Template("Project/Task", mount + "/Work/houdini/render"),
        Template("Project/Task", mount + "/Publish"),
    ])

    template = Template("Project/Task", mount + "/Work/maya/workspace.mel")
    template.source = os.path.join(os.path.dirname(__file__), "workspace.mel")
    templates.append(template)

    return templates
