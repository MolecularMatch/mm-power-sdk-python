# mm_power_sdk_python.ClinicalTrialApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trial**](ClinicalTrialApi.md#get_trial) | **GET** /trial/:id | Get a Clinical Trial

# **get_trial**
> ClinicalTrial get_trial(id)

Get a Clinical Trial

Get a Clinical Trial

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.ClinicalTrialApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Clinical Trial to return

try:
    # Get a Clinical Trial
    api_response = api_instance.get_trial(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClinicalTrialApi->get_trial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Clinical Trial to return | 

### Return type

[**ClinicalTrial**](ClinicalTrial.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

