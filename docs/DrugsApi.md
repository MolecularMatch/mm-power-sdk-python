# mm_power_sdk_python.DrugsApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drug**](DrugsApi.md#get_drug) | **GET** /drug/{id} | Get a Drug
[**search_drugs**](DrugsApi.md#search_drugs) | **POST** /drug/search | Search for drugs

# **get_drug**
> Drug get_drug(id)

Get a Drug

Get a drug

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.DrugsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Drug to return

try:
    # Get a Drug
    api_response = api_instance.get_drug(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrugsApi->get_drug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Drug to return | 

### Return type

[**Drug**](Drug.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **search_drugs**
> SearchResponseDrug search_drugs(body)

Search for drugs

Search for drugs

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.DrugsApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Search for drugs
    api_response = api_instance.search_drugs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrugsApi->search_drugs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponseDrug**](SearchResponseDrug.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

 

