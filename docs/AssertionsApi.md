# mm_power_sdk_python.AssertionsApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_assertions**](AssertionsApi.md#search_assertions) | **POST** /assertion/search | Search for assertions

# **search_assertions**
> SearchResponseDrug search_assertions(body)

Search for assertions

Search for evidence backed assertions

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponseDrug**](SearchResponseDrug.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) 

