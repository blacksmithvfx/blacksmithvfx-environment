import os

import pyblish.api


class BumpyboxDeadlineExtractEnvironment(pyblish.api.InstancePlugin):
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

        instance.data["deadlineData"] = {"job": job_data,
                                         "plugin": plugin_data}
