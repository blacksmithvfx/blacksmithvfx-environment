import os

import lucidity

from blacksmithvfx_environment import utils


def get_test_paths():
    return [
        "//disk/project_root/test_project",
        "//disk/project_root/test_project/in/elements",
        "//disk/project_root/test_project/in/footage/grade",
        "//disk/project_root/test_project/in/footage/raw",
        "//disk/project_root/test_project/in/roughCuts",
        "//disk/project_root/test_project/in/references/fromClient",
        "//disk/project_root/test_project/in/shoot/scriptNotes",
        "//disk/project_root/test_project/in/shoot/stills",
        "//disk/project_root/test_project/in/GFX",
        "//disk/project_root/test_project/in/assets",
        "//disk/project_root/test_project/in/EDL",
        "//disk/project_root/test_project/in/production/storyboards",
        "//disk/project_root/test_project/in/production/treatment",
        "//disk/project_root/test_project/in/production/script",
        "//disk/project_root/test_project/in/roto",
        "//disk/project_root/test_project/in/audio",
        "//disk/project_root/test_project/out/tracking",
        "//disk/project_root/test_project/out/mattePainting",
        "//disk/project_root/test_project/out/deliverables",
        "//disk/project_root/test_project/out/client",
        "//disk/project_root/test_project/out/cleanUp",
        "//disk/project_root/test_project/out/roto",

        "//disk/project_root/test_project/Tasks/editing",
        "//disk/project_root/test_project/Tasks/editing/Work/nuke/scripts",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/"
        "sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/autosave",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/scripts",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/images",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/data",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/sound",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/particles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/assets",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "bifrost",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "particles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "nCache",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "alembic",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/scenes/"
        "edit",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/clips",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/movies",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/iprImages",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/depth",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furFiles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furImages",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furShadowMap",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furEqualMap",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furAttrMap",
        "//disk/project_root/test_project/Tasks/editing/Work/flame",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/hip",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/tex",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/geo",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/sim",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/render",
        "//disk/project_root/test_project/Tasks/editing/Publish",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/"
        "workspace.mel",

        "//disk/project_root/test_project/Assets",

        "//disk/project_root/test_project/Assets/Character/rat",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "nuke",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "nuke/scripts",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/sourceimages",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/autosave",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/scripts",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/images",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/data",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/sound",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/particles",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/assets",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/cache",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/cache/bifrost",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/cache/particles",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/cache/nCache",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/cache/alembic",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/scenes",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/scenes/edit",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/clips",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/movies",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/iprImages",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/depth",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur/furFiles",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur/furImages",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "maya/renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "flame",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini/hip",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini/tex",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini/geo",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini/sim",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work/"
        "houdini/render",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/"
        "Publish",
        "//disk/project_root/test_project/Assets/Character/rat/Lookdev/Work"
        "/maya/workspace.mel",

        "//disk/project_root/test_project/Shots/sh0010",
        "//disk/project_root/test_project/Shots/sh0010/Footage",

        "//disk/project_root/test_project/Shots/sh0010/Animation",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/nuke",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/nuke/"
        "scripts",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "sound",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "clips",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "sourceimages",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "cache",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "cache/bifrost",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "cache/particles",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "cache/alembic",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "cache/nCache",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "scenes",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "scenes/edit",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "autosave",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "particles",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "movies",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur/furFiles",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur/furImages",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/depth",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "renderData/iprImages",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "scripts",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "images",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "data",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "assets",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/flame",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini/hip",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini/tex",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini/geo",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini/render",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/"
        "houdini/sim",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Publish",
        "//disk/project_root/test_project/Shots/sh0010/Animation/Work/maya/"
        "workspace.mel",

        "//disk/project_root/test_project/Sequences/sq001",

        "//disk/project_root/test_project/Sequences/sq001/sh0010",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Footage",

        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/nuke",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/nuke/scripts",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/sound",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/particles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/sourceimages",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/cache",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/cache/bifrost",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/cache/particles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/cache/nCache",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/cache/alembic",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/scenes",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/scenes/edit",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/autosave",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/clips",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/movies",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/iprImages",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/depth",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur/furFiles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur/furImages",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/scripts",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/images",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/data",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/assets",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/flame",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini/hip",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini/tex",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini/geo",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini/sim",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/houdini/render",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Publish",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Compositing"
        "/Work/maya/workspace.mel",
    ]


def assert_entity(entity):
    templates = lucidity.discover_templates()
    msg = (
        "No valid templates found for template name: \"{0}\", and entity: "
        "\"{1}\"".format(templates[0].get_template_name(entity), entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg

    get_resolved_paths(entity)


def get_resolved_paths(entity):
    templates = lucidity.discover_templates()
    valid_templates = templates[0].get_valid_templates(entity, templates)
    resolved_paths = []
    for template in valid_templates:
        try:
            resolved_paths.append(template.format(entity))
        except lucidity.error.FormatError as e:
            msg = e.message + "\nTemplate name: {0}".format(template.name)
            raise type(e)(msg)

    return resolved_paths


def get_workfile_extensions():
    return [".nk", ".mb", ".hip"]


def get_imagefile_extensions():
    return [".exr", ".dpx", ".jpeg", ".jpg", ".hdr"]


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in paths:
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in template_paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def test_unused_templates():
    templates = lucidity.discover_templates()

    used_templates = []
    for entity in get_entities():
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg


def test_excess_templates():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def test_project():
    project = utils.mock_entity(
        ("disk", {"windows": "//disk", "unix": "//disk"}),
        ("root", "project_root"),
        ("name", "test_project"),
        entity_type="Project"
    )
    assert_entity(project)

    return project


def test_project_editing():
    entities = []

    project = test_project()

    # project/editing
    task = utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )
    assert_entity(task)
    entities.append(task)

    return entities


def get_entities():
    entities = []
    entities.append(test_project())
    entities.extend(test_project_editing())
    return entities
