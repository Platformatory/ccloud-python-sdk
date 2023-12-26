# openapi_client.ConsumerSharedResourcesCdxV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cdx_v1_consumer_shared_resource**](ConsumerSharedResourcesCdxV1Api.md#get_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id} | Read a Consumer Shared Resource
[**image_cdx_v1_consumer_shared_resource**](ConsumerSharedResourcesCdxV1Api.md#image_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id}/images/{file_name} | Get image for shared resource
[**list_cdx_v1_consumer_shared_resources**](ConsumerSharedResourcesCdxV1Api.md#list_cdx_v1_consumer_shared_resources) | **GET** /cdx/v1/consumer-shared-resources | List of Consumer Shared Resources
[**network_cdx_v1_consumer_shared_resource**](ConsumerSharedResourcesCdxV1Api.md#network_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id}:network | Get shared resource&#39;s network configuration


# **get_cdx_v1_consumer_shared_resource**
> bool, date, datetime, dict, float, int, list, str, none_type get_cdx_v1_consumer_shared_resource(id)

Read a Consumer Shared Resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a consumer shared resource.

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_shared_resources__cdx_v1_api
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
    api_instance = consumer_shared_resources__cdx_v1_api.ConsumerSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the consumer shared resource.

    # example passing only required values which don't have defaults set
    try:
        # Read a Consumer Shared Resource
        api_response = api_instance.get_cdx_v1_consumer_shared_resource(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerSharedResourcesCdxV1Api->get_cdx_v1_consumer_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the consumer shared resource. |

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
**200** | Consumer Shared Resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_cdx_v1_consumer_shared_resource**
> file_type image_cdx_v1_consumer_shared_resource(id, file_name)

Get image for shared resource

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Returns the image file for the shared resource

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_shared_resources__cdx_v1_api
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
    api_instance = consumer_shared_resources__cdx_v1_api.ConsumerSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the consumer shared resource.
    file_name = "file_name_example" # str | The File Name

    # example passing only required values which don't have defaults set
    try:
        # Get image for shared resource
        api_response = api_instance.image_cdx_v1_consumer_shared_resource(id, file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerSharedResourcesCdxV1Api->image_cdx_v1_consumer_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the consumer shared resource. |
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
**200** | Returns the image file&#39;s binary content |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cdx_v1_consumer_shared_resources**
> bool, date, datetime, dict, float, int, list, str, none_type list_cdx_v1_consumer_shared_resources()

List of Consumer Shared Resources

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all consumer shared resources.

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_shared_resources__cdx_v1_api
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
    api_instance = consumer_shared_resources__cdx_v1_api.ConsumerSharedResourcesCdxV1Api(api_client)
    stream_share = "ss-1234" # str | Filter the results by exact match for stream_share. (optional)
    include_deleted = True # bool | Include deactivated shared resources (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 10
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Consumer Shared Resources
        api_response = api_instance.list_cdx_v1_consumer_shared_resources(stream_share=stream_share, include_deleted=include_deleted, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerSharedResourcesCdxV1Api->list_cdx_v1_consumer_shared_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_share** | **str**| Filter the results by exact match for stream_share. | [optional]
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
**200** | Consumer Shared Resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_cdx_v1_consumer_shared_resource**
> CdxV1Network network_cdx_v1_consumer_shared_resource(id)

Get shared resource's network configuration

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Returns network information of the shared resource

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_shared_resources__cdx_v1_api
from openapi_client.model.failure import Failure
from openapi_client.model.cdx_v1_network import CdxV1Network
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
    api_instance = consumer_shared_resources__cdx_v1_api.ConsumerSharedResourcesCdxV1Api(api_client)
    id = "id_example" # str | The unique identifier for the consumer shared resource.

    # example passing only required values which don't have defaults set
    try:
        # Get shared resource's network configuration
        api_response = api_instance.network_cdx_v1_consumer_shared_resource(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerSharedResourcesCdxV1Api->network_cdx_v1_consumer_shared_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the consumer shared resource. |

### Return type

[**CdxV1Network**](CdxV1Network.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The network information of the shared resource |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

