# Welcome to the MMPower Python SDK

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/MolecularMatch/mm-power-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/MolecularMatch/mm-power-sdk-python.git`)

Then import the package:
```python
import mm_power_sdk_python 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mm_power_sdk_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from mm_power_sdk_python.configuration import Configuration
from pprint import pprint

# setup configuration with your api key
configuration = Configuration()
configuration.api_key = "<insert your api key here>"

# create an instance of the API class
api_instance = mm_power_sdk_python.AssertionsApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Search for assertions
    api_response = api_instance.search_assertions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertionsApi->search_assertions: %s\n" % e)
```
