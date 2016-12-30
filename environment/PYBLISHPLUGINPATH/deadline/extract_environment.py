import os

import pyblish.api
import pyblish_bumpybox
import pyblish_ftrack
import pyblish_deadline


class BlacksmithDeadlineExtractEnvironment(pyblish.api.InstancePlugin):
    """ Appending Ftrack enviroment variables to Deadline job. """

    order = pyblish.api.ExtractorOrder
    families = ["deadline"]
    label = "Environment"

    def process(self, instance):

        # Get plugin and job data.
        job_data = {}
        plugin_data = {}
        if instance.has_data('deadlineData'):
            job_data = instance.data('deadlineData')['job'].copy()
            plugin_data = instance.data('deadlineData')['plugin'].copy()

        key = "FTRACK_SERVER={0}".format(os.environ["FTRACK_SERVER"])
        job_data["EnvironmentKeyValue0"] = key
        key = "FTRACK_APIKEY={0}".format(os.environ["FTRACK_APIKEY"])
        job_data["EnvironmentKeyValue1"] = key
        key = "LOGNAME={0}".format(os.environ["LOGNAME"])
        job_data["EnvironmentKeyValue2"] = key
        key = "PYTHONPATH={0}".format(os.environ["PYTHONPATH"])
        job_data["EnvironmentKeyValue3"] = key
        key = "FTRACK_TEMPLATES_PATH={0}".format(
            os.environ["FTRACK_TEMPLATES_PATH"]
        )
        job_data["EnvironmentKeyValue4"] = key
        key = "FTRACK_TASKID={0}".format(os.environ["FTRACK_TASKID"])
        job_data["EnvironmentKeyValue5"] = key

        # OnJobFinished
        paths = os.path.join(
            os.path.dirname(pyblish_bumpybox.__file__),
            "plugins",
            "deadline",
            "OnJobFinished"
        )
        paths += os.pathsep
        paths += os.path.join(
            os.path.dirname(pyblish_ftrack.__file__), "plugins"
        )
        paths += os.pathsep
        paths += os.path.join(os.path.dirname(__file__), "OnJobFinished")
        key = "OnJobFinishedPaths={0}".format(paths)
        job_data["EnvironmentKeyValue6"] = key

        # OnJobSubmitted
        paths = os.path.join(
            os.path.dirname(pyblish_bumpybox.__file__),
            "plugins",
            "deadline",
            "OnJobSubmitted"
        )
        paths += os.pathsep
        paths += os.path.join(
            os.path.dirname(pyblish_deadline.__file__), "plugins"
        )
        key = "OnJobSubmittedPaths={0}".format(paths)
        job_data["EnvironmentKeyValue7"] = key

        instance.data["deadlineData"] = {"job": job_data,
                                         "plugin": plugin_data}
