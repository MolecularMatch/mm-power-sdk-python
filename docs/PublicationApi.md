# mm_power_sdk_python.PublicationApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_publications**](PublicationApi.md#count_publications) | **POST** /publication/count | Get the count of Publications matching a searchRequest
[**get_publication**](PublicationApi.md#get_publication) | **GET** /publication/{id} | Get a Publication
[**search_publications**](PublicationApi.md#search_publications) | **POST** /publication/search | Search for Publications

# **count_publications**
> SearchResponsePublication count_publications(body)

Get the count of Publications matching a searchRequest

Get the count of Publications matching a searchRequest

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.PublicationApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Get the count of Publications matching a searchRequest
    api_response = api_instance.count_publications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationApi->count_publications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponsePublication**](SearchResponsePublication.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

 

# **get_publication**
> Publication get_publication(id)

Get a Publication

Get a Publication

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.PublicationApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Publication to return

try:
    # Get a Publication
    api_response = api_instance.get_publication(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationApi->get_publication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Publication to return | 

### Return type

[**Publication**](Publication.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **search_publications**
> SearchResponsePublication search_publications(body)

Search for Publications

Search for Publications

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.PublicationApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Search for Publications
    api_response = api_instance.search_publications(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationApi->search_publications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| SearchRequest object to send to MolecularMatch for processing | 

### Return type

[**SearchResponsePublication**](SearchResponsePublication.md)





### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

 

