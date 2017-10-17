import os

import ftrack_api
import ftrack_template


def modify_launch(event):
    """Return directories and files to create."""

    for entity in event["data"].get("entities", []):

        templates = ftrack_template.discover_templates()
        valid_templates = ftrack_template.format(
            {}, templates, entity, return_mode="all"
        )

        for path, template in valid_templates:

            if template.isfile:
                if not os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))

                if not os.path.exists(path):
                    event["data"]["files"].append((template.source, path))
            else:
                if not os.path.exists(path):
                    event["data"]["directories"].append(path)

    return event


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    session.event_hub.subscribe('topic=create_structure.launch', modify_launch)
