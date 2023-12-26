# openapi_client.ProviderSharedResourcesCdxV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_image_cdx_v1_provider_shared_resource**](ProviderSharedResourcesCdxV1Api.md#delete_image_cdx_v1_provider_shared_resource) | **DELETE** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Delete the shared resource&#39;s image
[**get_cdx_v1_provider_shared_resource**](ProviderSharedResourcesCdxV1Api.md#get_cdx_v1_provider_shared_resource) | **GET** /cdx/v1/provider-shared-resources/{id} | Read a Provider Shared Resource
[**list_cdx_v1_provider_shared_resources**](ProviderSharedResourcesCdxV1Api.md#list_cdx_v1_provider_shared_resources) | **GET** /cdx/v1/provider-shared-resources | List of Provider Shared Resources
[**update_cdx_v1_provider_shared_resource**](ProviderSharedResourcesCdxV1Api.md#update_cdx_v1_provider_shared_resource) | **PATCH** /cdx/v1/provider-shared-resources/{id} | Update a Provider Shared Resource
[**upload_image_cdx_v1_provider_shared_resource**](ProviderSharedResourcesCdxV1Api.md#upload_image_cdx_v1_provider_shared_resource) | **POST** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Upload image for shared resource
[**view_image_cdx_v1_provider_shared_resource**](ProviderSharedResourcesCdxV1Api.md#view_image_cdx_v1_provider_shared_resource) | **GET** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Get image for shared resource


# **delete_image_cdx_v1_provider_shared_resource**
> delete_image_cdx_v1_provider_shared_resource(id, file_name)

Delete the shared resource's image

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Deletes the image file for the shared resource

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the provider shared resource.
    file_name = "file_name_example" # str | The File Name

    # example passing only required values which don't have defaults set
    try:
        # Delete the shared resource's image
        api_instance.delete_image_cdx_v1_provider_shared_resource(id, file_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->delete_image_cdx_v1_provider_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the provider shared resource. |
 **file_name** | **str**| The File Name |

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdx_v1_provider_shared_resource**
> bool, date, datetime, dict, float, int, list, str, none_type get_cdx_v1_provider_shared_resource(id)

Read a Provider Shared Resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a provider shared resource.

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the provider shared resource.

    # example passing only required values which don't have defaults set
    try:
        # Read a Provider Shared Resource
        api_response = api_instance.get_cdx_v1_provider_shared_resource(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->get_cdx_v1_provider_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the provider shared resource. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider Shared Resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cdx_v1_provider_shared_resources**
> bool, date, datetime, dict, float, int, list, str, none_type list_cdx_v1_provider_shared_resources()

List of Provider Shared Resources

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all provider shared resources.

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    stream_share = "ss-1234" # str | Filter the results by exact match for stream_share. (optional)
    crn = "crn://confluent.cloud/cloud-cluster=lkc-111aaa/kafka=lkc-111aaa/topic=my.topic" # str | Filter the results by exact match for crn. (optional)
    include_deleted = True # bool | Include deactivated shared resources (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 10
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Provider Shared Resources
        api_response = api_instance.list_cdx_v1_provider_shared_resources(stream_share=stream_share, crn=crn, include_deleted=include_deleted, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->list_cdx_v1_provider_shared_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_share** | **str**| Filter the results by exact match for stream_share. | [optional]
 **crn** | **str**| Filter the results by exact match for crn. | [optional]
 **include_deleted** | **bool**| Include deactivated shared resources | [optional]
 **page_size** | **int**| A pagination size for collection requests. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider Shared Resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cdx_v1_provider_shared_resource**
> bool, date, datetime, dict, float, int, list, str, none_type update_cdx_v1_provider_shared_resource(id)

Update a Provider Shared Resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a provider shared resource.  

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from openapi_client.model.cdx_v1_provider_shared_resource_update import CdxV1ProviderSharedResourceUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the provider shared resource.
    cdx_v1_provider_shared_resource_update = CdxV1ProviderSharedResourceUpdate(
        metadata=None,
        resources=[
            "crn://confluent.cloud/environment=env-123/cloud-cluster=lkc-111aaa/kafka=lkc-111aaa/topic=my.topic",
        ],
        display_name="Stock Trades",
        organization_description="ABC Corp is the biggest online retailer",
        organization_contact="jane.doe@example.com",
    ) # CdxV1ProviderSharedResourceUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Provider Shared Resource
        api_response = api_instance.update_cdx_v1_provider_shared_resource(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->update_cdx_v1_provider_shared_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Provider Shared Resource
        api_response = api_instance.update_cdx_v1_provider_shared_resource(id, cdx_v1_provider_shared_resource_update=cdx_v1_provider_shared_resource_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->update_cdx_v1_provider_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the provider shared resource. |
 **cdx_v1_provider_shared_resource_update** | [**CdxV1ProviderSharedResourceUpdate**](CdxV1ProviderSharedResourceUpdate.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider Shared Resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image_cdx_v1_provider_shared_resource**
> upload_image_cdx_v1_provider_shared_resource(id, file_name)

Upload image for shared resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Upload the image file for the shared resource

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the provider shared resource.
    file_name = "file_name_example" # str | The File Name
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload image for shared resource
        api_instance.upload_image_cdx_v1_provider_shared_resource(id, file_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->upload_image_cdx_v1_provider_shared_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload image for shared resource
        api_instance.upload_image_cdx_v1_provider_shared_resource(id, file_name, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->upload_image_cdx_v1_provider_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the provider shared resource. |
 **file_name** | **str**| The File Name |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | image uploaded |  * Location - A URL that allows access to the resourced named by the crn <br>  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_image_cdx_v1_provider_shared_resource**
> file_type view_image_cdx_v1_provider_shared_resource(id, file_name)

Get image for shared resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Returns the image file for the shared resource

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import provider_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_shared_resources__cdx_v1_api.ProviderSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the provider shared resource.
    file_name = "file_name_example" # str | The File Name

    # example passing only required values which don't have defaults set
    try:
        # Get image for shared resource
        api_response = api_instance.view_image_cdx_v1_provider_shared_resource(id, file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProviderSharedResourcesCdxV1Api->view_image_cdx_v1_provider_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the provider shared resource. |
 **file_name** | **str**| The File Name |

### Return type

**file_type**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the image file |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

