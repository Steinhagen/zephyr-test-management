from zephyr.common.cloud.endpoints import TestCaseEndpoints
from .paths import ScaleCloudPaths as Paths


class ScaleTestCaseEndpoints(TestCaseEndpoints):
    """
    Api wrapper for "Test Case" endpoints

    Details: https://support.smartbear.com/zephyr-scale-cloud/api-docs/#tag/Test-Cases
    """

    def get_versions(self, test_case_key: str, **kwargs):
        """
        Returns all test case versions for a test case with specified key.
        Response is ordered by most recent first
        """
        return self.session.get_paginated(Paths.CASE_VERS.format(test_case_key),
                                          params=kwargs)

    def get_version(self, test_case_key: str, version: str):
        """Retrieves a specific version of a test case."""
        return self.session.get(Paths.CASE_VER.format(test_case_key, version))
