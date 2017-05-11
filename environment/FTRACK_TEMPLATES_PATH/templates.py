import os
import platform

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
    task = "{#task.name}"
    tasks = "Tasks/" + task
    assetversion = "{#assetversion.asset.type.short}/v{#assetversion.version}"
    file_component = "{#component.name}{#component.file_type}"
    sequence_component = (
        "{#container.name}/{#container.name}.{#component.name}" +
        "{#component.file_type}"
    )
    assets = "Assets/{#assetbuild.type.name}/{#assetbuild.name}"
    shot = "{#shot.name}"
    shots = "Shots/" + shot
    sequence = "{#sequence.name}"
    sequences = "Sequences/" + sequence
    episode = "{#episode.name}"
    episodes = "Episodes/" + episode

    # Files included in structure
    workspace_file = os.path.join(os.path.dirname(__file__), "workspace.mel")

    # Structures
    task_structure = {
        "Publish": {
            assetversion: {
                file_component: {},
                sequence_component: {}
            }
        },
        "Work": {
            "flame": {},
            "{houdini}": {
                "hip": {
                    "houdini_v{padded_version}.hip": {},
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
                    "maya_v{padded_version}.mb": {},
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
                    "edit": {},
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
                    "nuke_v{padded_version}.nk": {},
                }
            },
        }
    }

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
                task: task_structure,
                assets: {
                    task: task_structure
                },
            },
            sequences: {
                task: task_structure,
                assets: {
                    task: task_structure
                },
                shot: {
                    task: task_structure,
                    assets: {
                        task: task_structure
                    }
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
                    }
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
                        }
                    }
                },
            }
        }
    }

    return dictionary_to_paths(project_structure)
