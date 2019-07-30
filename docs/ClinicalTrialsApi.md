# mm_power_sdk_python.ClinicalTrialsApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_trials**](ClinicalTrialsApi.md#count_trials) | **POST** /trial/count | Get the count of Clinical Trials matching a searchRequest
[**get_trial**](ClinicalTrialsApi.md#get_trial) | **GET** /trial/{id} | Get a Clinical Trial
[**search_trials**](ClinicalTrialsApi.md#search_trials) | **POST** /trial/search | Search for clinical trials

# **count_trials**
> SearchResponseClinicalTrial count_trials(body)

Get the count of Clinical Trials matching a searchRequest

Get the count of Clinical Trials matching a searchRequest

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.ClinicalTrialsApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Get the count of Clinical Trials matching a searchRequest
    api_response = api_instance.count_trials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClinicalTrialsApi->count_trials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponseClinicalTrial**](SearchResponseClinicalTrial.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

 

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
api_instance = mm_power_sdk_python.ClinicalTrialsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Clinical Trial to return

try:
    # Get a Clinical Trial
    api_response = api_instance.get_trial(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClinicalTrialsApi->get_trial: %s\n" % e)
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

 

# **search_trials**
> SearchResponseClinicalTrial search_trials(body)

Search for clinical trials

Search for clinical trials

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.ClinicalTrialsApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Search for clinical trials
    api_response = api_instance.search_trials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClinicalTrialsApi->search_trials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponseClinicalTrial**](SearchResponseClinicalTrial.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

 

