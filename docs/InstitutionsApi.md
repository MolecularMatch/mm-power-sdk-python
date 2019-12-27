# mm_power_sdk_python.InstitutionsApi

All URIs are relative to *https://api.molecularmatch.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_institution**](InstitutionsApi.md#delete_institution) | **DELETE** /institution/{id} | Delete an institution
[**get_institution**](InstitutionsApi.md#get_institution) | **GET** /institution/{id} | Get an institution
[**get_institution_status**](InstitutionsApi.md#get_institution_status) | **GET** /institution/{id}/status | Get an institution record&#x27;s status
[**institution_post**](InstitutionsApi.md#institution_post) | **POST** /institution | Create an institution
[**institutions_get**](InstitutionsApi.md#institutions_get) | **GET** /institutions | Get a paginated list of institutions
[**put_institution**](InstitutionsApi.md#put_institution) | **PUT** /institution/{id} | Put/Update an institution

# **delete_institution**
> Institution delete_institution(id)

Delete an institution

Delete an institution

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Institution to delete

try:
    # Delete an institution
    api_response = api_instance.delete_institution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->delete_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Institution to delete | 

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **get_institution**
> Institution get_institution(id)

Get an institution

Get an institution

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Institution to return

try:
    # Get an institution
    api_response = api_instance.get_institution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->get_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Institution to return | 

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **get_institution_status**
> Institution get_institution_status(id)

Get an institution record's status

Get an institution status

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Institution to return status for

try:
    # Get an institution record's status
    api_response = api_instance.get_institution_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->get_institution_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Institution to return status for | 

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **institution_post**
> Institution institution_post()

Create an institution

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))

try:
    # Create an institution
    api_response = api_instance.institution_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institution_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **institutions_get**
> Institution institutions_get()

Get a paginated list of institutions

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))

try:
    # Get a paginated list of institutions
    api_response = api_instance.institutions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institutions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

# **put_institution**
> Institution put_institution(id)

Put/Update an institution

Put an institution

### Example
```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.InstitutionsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Institution to return

try:
    # Put/Update an institution
    api_response = api_instance.put_institution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->put_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Institution to return | 

### Return type

[**Institution**](Institution.md)





### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

 

