import os
import platform
import copy

import ftrack_template


def dictionary_to_paths(data, path="", results=[]):

    for key, value in data.iteritems():

        parent_path = (path + os.sep + key)
        if not path:
            parent_path = key

        if isinstance(value, dict):
            if "isfile" in value:
                temp = ftrack_template.Template("template", parent_path)
                temp.isfile = value["isfile"]
                temp.source = value["source"]
                results.append(temp)
            else:
                temp = ftrack_template.Template("template", parent_path)
                temp.isfile = False
                results.append(temp)
                if value:
                    dictionary_to_paths(
                        value, path=parent_path, results=results
                    )

    return results


def register():
    '''Register templates.'''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    # Common Ftrack entity paths
    mount = (
        "{#project.disk." + system_name + "}/{#project.root}/{#project.name}"
    )
    task = "{#task.type.name}"
    tasks = "Tasks/" + task
    assets = "Assets/{#assetbuild.type.name}/{#assetbuild.name}"
    shot = "{#shot.name}"
    shots = "Shots/" + shot
    sequence = "{#sequence.name}"
    sequences = "Sequences/" + sequence
    episode = "{#episode.name}"
    episodes = "Episodes/" + episode

    # Work Structure
    workspace_file = os.path.join(os.path.dirname(__file__), "workspace.mel")
    work_file_name = "{#task.type.name}_{#task.name}"
    work_file_name += "_v{padded_version}"
    houdini_work_file = work_file_name + ".hip"
    maya_work_file = work_file_name + ".mb"
    nuke_work_file = work_file_name + ".nk"
    task_structure = {
        "Work": {
            "flame": {},
            "{houdini}": {
                "hip": {
                    "{#task.name}": {
                        houdini_work_file: {}
                    }
                }
            },
            "houdini": {
                "geo": {},
                "hip": {},
                "render": {},
                "sim": {},
                "tex": {},
            },
            "{maya}": {
                "scenes": {
                    "{#task.name}": {
                        maya_work_file: {}
                    }
                }
            },
            "maya": {
                "assets": {},
                "autosave": {},
                "cache": {
                    "alembic": {},
                    "bifrost": {},
                    "nCache": {},
                    "particles": {}
                },
                "clips": {},
                "data": {},
                "images": {},
                "movies": {},
                "particles": {},
                "renderData": {
                    "depth": {},
                    "fur": {
                        "furAttrMap": {},
                        "furEqualMap": {},
                        "furFiles": {},
                        "furImages": {},
                        "furShadowMap": {}
                    },
                    "iprImages": {}
                },
                "scenes": {
                    "edit": {}
                },
                "scripts": {},
                "sound": {},
                "sourceimages": {
                    "3dPaintTextures": {}
                },
                "workspace.mel": {"isfile": True, "source": workspace_file},
            },
            "{nuke}": {
                "scripts": {
                    "{#task.name}": {
                        nuke_work_file: {}
                    }
                }
            },
            "nuke": {
                "scripts": {},
                "renders": {
                	"precomp": {},
                	"comp": {},
                	"slapcomp": {},
                },
            },
        }
    }

    # Publish structure
    publish_path = (
        "{#assetversion.asset.type.short}/{#asset.name}/" +
        "v{#assetversion.version}"
    )
    file_component = (
        "{#task.parent.name}_{#task.type.name}_{#component.name}_" +
        "v{#assetversion.version}{#component.file_type}"
    )
    sequence_component = (
        "{#task.parent.name}_{#task.type.name}_{#container.name}_" +
        "v{#assetversion.version}.{#component.name}{#component.file_type}"
    )
    task_structure["Publish"] = {
        publish_path: {
            file_component: {},
            sequence_component: {}
        }
    }

    # Shot structure
    shot_task_structure = copy.deepcopy(task_structure)
    work_file = "{#shot.name}_" + work_file_name + ".hip"
    shot_task_structure["Work"]["{houdini}"]["hip"] = {work_file: {}}
    work_file = "{#shot.name}_" + work_file_name + ".mb"
    shot_task_structure["Work"]["{maya}"]["scenes"] = {work_file: {}}
    work_file = "{#shot.name}_" + work_file_name + ".nk"
    shot_task_structure["Work"]["{nuke}"]["scripts"] = {work_file: {}}

    # Sequence structure
    sequence_task_structure = copy.deepcopy(task_structure)
    work_file = "{#sequence.name}_" + work_file_name + ".hip"
    sequence_task_structure["Work"]["{houdini}"]["hip"] = {work_file: {}}
    work_file = "{#sequence.name}_" + work_file_name + ".mb"
    sequence_task_structure["Work"]["{maya}"]["scenes"] = {work_file: {}}
    work_file = "{#sequence.name}_" + work_file_name + ".nk"
    sequence_task_structure["Work"]["{nuke}"]["scripts"] = {work_file: {}}

    # Sequence/Shot structure
    sequence_shot_task_structure = copy.deepcopy(shot_task_structure)
    work_file = "{#sequence.name}_{#shot.name}_" + work_file_name + ".hip"
    sequence_shot_task_structure["Work"]["{houdini}"]["hip"] = {work_file: {}}
    work_file = "{#sequence.name}_{#shot.name}_" + work_file_name + ".mb"
    sequence_shot_task_structure["Work"]["{maya}"]["scenes"] = {work_file: {}}
    work_file = "{#sequence.name}_{#shot.name}_" + work_file_name + ".nk"
    sequence_shot_task_structure["Work"]["{nuke}"]["scripts"] = {work_file: {}}

    publish_path = (
        "{#assetversion.asset.type.short}/{#asset.name}/" +
        "v{#assetversion.version}"
    )
    file_component = (
        "{#sequence.name}_{#task.parent.name}_{#task.type.name}_" +
        "{#component.name}_v{#assetversion.version}{#component.file_type}"
    )
    sequence_component = (
        "{#sequence.name}_{#task.parent.name}_{#task.type.name}_" +
        "{#container.name}_v{#assetversion.version}.{#component.name}" +
        "{#component.file_type}"
    )
    sequence_shot_task_structure["Publish"] = {
        publish_path: {
            file_component: {},
            sequence_component: {}
        }
    }

    # Entire structure
    project_structure = {
        mount: {
            "in": {
                "assets": {},
                "audio": {},
                "EDL": {},
                "elements": {},
                "GFX": {},
                "roto": {},
                "roughCuts": {},
                "footage": {
                    "raw": {},
                    "grade": {},
                },
                "production": {
                    "script": {},
                    "storyboards": {},
                    "treatment": {},
                },
                "references": {
                    "fromClient": {},
                },
                "shoot": {
                    "scriptNotes": {},
                    "stills": {},
                },
            },
            "out": {
                "cleanUp": {},
                "client": {},
                "deliverables": {},
                "mattePainting": {},
                "roto": {},
                "tracking": {},
            },
            tasks: task_structure,
            assets: {
                task: task_structure
            },
            shots: {
                task: shot_task_structure,
                assets: {
                    task: shot_task_structure
                },
                "Footage": {}
            },
            sequences: {
                task: sequence_task_structure,
                assets: {
                    task: sequence_task_structure
                },
                shot: {
                    task: sequence_shot_task_structure,
                    assets: {
                        task: sequence_shot_task_structure
                    },
                    "Footage": {}
                }
            },
            episodes: {
                task: task_structure,
                assets: {
                    task: task_structure
                },
                shot: {
                    task: task_structure,
                    assets: {
                        task: task_structure
                    },
                    "Footage": {}
                },
                sequence: {
                    task: task_structure,
                    assets: {
                        task: task_structure
                    },
                    shot: {
                        task: task_structure,
                        assets: {
                            task: task_structure
                        },
                        "Footage": {}
                    }
                },
            }
        }
    }

    return dictionary_to_paths(project_structure)
