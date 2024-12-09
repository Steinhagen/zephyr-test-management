"""Paths to form Cloud API URLs"""

from zephyr.common.cloud.endpoints.paths import CloudPaths

class ScaleCloudPaths(CloudPaths):
    """
    Zephyr Scale Cloud API paths based on:
    https://support.smartbear.com/zephyr-scale-cloud/api-docs/
    """
    # Test Cases
    CASE_VERS = "testcases/{}/versions"
    CASE_VER = "testcases/{}/versions/{}"
