# Zephyr Test Management


![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zephyr-test-management)
![PyPI](https://img.shields.io/pypi/v/zephyr-test-management)
![PyPI - License](https://img.shields.io/pypi/l/zephyr-test-management)

### Project description
This is a set of wrappers for both Zephyr Scale and Zephyr Squad (TM4J) REST APIs.
This means you can interact with Zephyr without GUI, access it with python code and create
automation scripts for your every day interactions.

This project is a fork of nassauwinter's [zephyr-python-api](https://github.com/nassauwinter/zephyr-python-api).

For more detailed information please see [the project's documentation](https://zephyr-test-management.readthedocs.io/en/latest/index.html).

To be done:
* Zephyr Squad Cloud support
* More usage examples for cloud versions
* Increase the tests coverage
* Convenient docs
* Implementing higher level wrappers representing Test Case, Test Cycle, etc.

## Installation

```
pip install zephyr-test-management
```

## Example usage

### Zephyr Scale

Zephyr Scale Cloud auth:
```python
from zephyr import ZephyrScale

zscale = ZephyrScale(token="<your_token>")
```

Zephyr Scale Server (TM4J) auth:
```python
from zephyr import ZephyrScale

# Auth can be made with Jira token
auth = {"token": "<your_jira_token>"}

# or with login and password (suggest using get_pass)
auth = {"username": "<your_login>", "password": "<your_password>"}

# or even session cookie dict
auth = {"cookies": "<session_cookie_dict>"}

zscale = ZephyrScale.server_api(base_url="<your_base_url>", **auth)
```

Then it is possible to interact with api wrappers:
```python
zapi = zscale.api

# Get all test cases
all_test_cases = zapi.test_cases.get_test_cases()

# Get a single test case by its id
test_case = zapi.test_cases.get_test_case("<test_case_id>")

# Create a test case
creation_result = zapi.test_cases.create_test_case("<project_key>", "test_case_name")
```

### Zephyr Squad

Zephyr Squad Server (TM4J) auth:
```python
from zephyr import ZephyrSquad

# Auth can be made with Jira token
auth = {"token": "<your_jira_token>"}

# or with login and password (suggest using get_pass)
auth = {"username": "<your_login>", "password": "<your_password>"}

# or even session cookie dict
auth = {"cookies": "<session_cookie_dict>"}

zsquad = ZephyrSquad(base_url=base_url, **auth)
```

Then it is possible to interact with api wrappers:
```python
# Obtain a project's information
project_info = zsquad.actions.project.get_project_info("<project_key>")

# Obtain a project's versions/releases
project_versions = zsquad.api.util_resource.get_all_versions("<project_id>")

# Get a single test case by its id
test_case = zsquad.actions.test_cases.get_test_case("<case_key>", fields="id")

# Create a new test case for a project
data = {
    "fields": {
        "assignee": {
            "name": "<jira_username>"
        },
        "description": "<case_description>"
    }
}
creation_result = zsquad.actions.test_cases.create_test_case(projectId="<project_id>", summary="<case_summary>", data=data)
```

## Troubleshooting

For troubleshooting see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)


## License

This library is licensed under the Apache 2.0 License.

## Links

[Zephyr Scale Cloud API docs](https://support.smartbear.com/zephyr-scale-cloud/api-docs/)

[Zephyr Scale Server API docs](https://support.smartbear.com/zephyr-scale-server/api-docs/v1/)

[Zephyr Squad Cloud API docs](https://smartbear.portal.swaggerhub.com/zephyr-squad/default/introduction)

[Zephyr Squad Server API docs](https://zephyrsquadserver.docs.apiary.io/)

[Zephyr Squad Server How to API docs](https://support.smartbear.com/zephyr-squad-server/docs/api/index.html)
