# openapi_client.NetworksNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_networking_v1_network**](NetworksNetworkingV1Api.md#create_networking_v1_network) | **POST** /networking/v1/networks | Create a Network
[**delete_networking_v1_network**](NetworksNetworkingV1Api.md#delete_networking_v1_network) | **DELETE** /networking/v1/networks/{id} | Delete a Network
[**get_networking_v1_network**](NetworksNetworkingV1Api.md#get_networking_v1_network) | **GET** /networking/v1/networks/{id} | Read a Network
[**list_networking_v1_networks**](NetworksNetworkingV1Api.md#list_networking_v1_networks) | **GET** /networking/v1/networks | List of Networks
[**update_networking_v1_network**](NetworksNetworkingV1Api.md#update_networking_v1_network) | **PATCH** /networking/v1/networks/{id} | Update a Network


# **create_networking_v1_network**
> bool, date, datetime, dict, float, int, list, str, none_type create_networking_v1_network()

Create a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a network.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import networks__networking_v1_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
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

# Configure OAuth2 access token for authorization: confluent-sts-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networks__networking_v1_api.NetworksNetworkingV1Api(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Network
        api_response = api_instance.create_networking_v1_network(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->create_networking_v1_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Network is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - Network resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_networking_v1_network**
> delete_networking_v1_network(environment, id)

Delete a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a network.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import networks__networking_v1_api
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

# Configure OAuth2 access token for authorization: confluent-sts-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networks__networking_v1_api.NetworksNetworkingV1Api(api_client)
    environment = "env-00000" # str | Scope the operation to the given environment.
    id = "id_example" # str | The unique identifier for the network.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Network
        api_instance.delete_networking_v1_network(environment, id)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->delete_networking_v1_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. |
 **id** | **str**| The unique identifier for the network. |

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A Network is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_networking_v1_network**
> bool, date, datetime, dict, float, int, list, str, none_type get_networking_v1_network(environment, id)

Read a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a network.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import networks__networking_v1_api
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

# Configure OAuth2 access token for authorization: confluent-sts-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networks__networking_v1_api.NetworksNetworkingV1Api(api_client)
    environment = "env-00000" # str | Scope the operation to the given environment.
    id = "id_example" # str | The unique identifier for the network.

    # example passing only required values which don't have defaults set
    try:
        # Read a Network
        api_response = api_instance.get_networking_v1_network(environment, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->get_networking_v1_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. |
 **id** | **str**| The unique identifier for the network. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_networking_v1_networks**
> bool, date, datetime, dict, float, int, list, str, none_type list_networking_v1_networks(environment)

List of Networks

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all networks.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import networks__networking_v1_api
from openapi_client.model.failure import Failure
from openapi_client.model.multiple_search_filter import MultipleSearchFilter
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

# Configure OAuth2 access token for authorization: confluent-sts-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networks__networking_v1_api.NetworksNetworkingV1Api(api_client)
    environment = "env-00000" # str | Filter the results by exact match for environment.
    spec_display_name = MultipleSearchFilter(["prod-gcp-us-central1","prod-aws-us-east1"]) # MultipleSearchFilter | Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. (optional)
    spec_cloud = MultipleSearchFilter(["GCP","AWS"]) # MultipleSearchFilter | Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. (optional)
    spec_region = MultipleSearchFilter(["us-central1","us-east-1"]) # MultipleSearchFilter | Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. (optional)
    spec_cidr = MultipleSearchFilter(["10.200.0.0/16"]) # MultipleSearchFilter | Filter the results by exact match for spec.cidr. Pass multiple times to see results matching any of the values. (optional)
    status_phase = MultipleSearchFilter(["PROVISIONING","READY"]) # MultipleSearchFilter | Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. (optional)
    connection_type = MultipleSearchFilter(["peering","privatelink"]) # MultipleSearchFilter | Filter the results by exact match for connection_type. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 10
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of Networks
        api_response = api_instance.list_networking_v1_networks(environment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->list_networking_v1_networks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Networks
        api_response = api_instance.list_networking_v1_networks(environment, spec_display_name=spec_display_name, spec_cloud=spec_cloud, spec_region=spec_region, spec_cidr=spec_cidr, status_phase=status_phase, connection_type=connection_type, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->list_networking_v1_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. |
 **spec_display_name** | **MultipleSearchFilter**| Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. | [optional]
 **spec_cloud** | **MultipleSearchFilter**| Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. | [optional]
 **spec_region** | **MultipleSearchFilter**| Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. | [optional]
 **spec_cidr** | **MultipleSearchFilter**| Filter the results by exact match for spec.cidr. Pass multiple times to see results matching any of the values. | [optional]
 **status_phase** | **MultipleSearchFilter**| Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. | [optional]
 **connection_type** | **MultipleSearchFilter**| Filter the results by exact match for connection_type. Pass multiple times to see results matching any of the values. | [optional]
 **page_size** | **int**| A pagination size for collection requests. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_networking_v1_network**
> bool, date, datetime, dict, float, int, list, str, none_type update_networking_v1_network(id)

Update a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a network.  

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import networks__networking_v1_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
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

# Configure OAuth2 access token for authorization: confluent-sts-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networks__networking_v1_api.NetworksNetworkingV1Api(api_client)
    id = "id_example" # str | The unique identifier for the network.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Network
        api_response = api_instance.update_networking_v1_network(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->update_networking_v1_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Network
        api_response = api_instance.update_networking_v1_network(id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworksNetworkingV1Api->update_networking_v1_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the network. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[api-key](../README.md#api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

