# openapi_client.IPGroupsIamV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iam_v2_ip_group**](IPGroupsIamV2Api.md#create_iam_v2_ip_group) | **POST** /iam/v2/ip-groups | Create an IP Group
[**delete_iam_v2_ip_group**](IPGroupsIamV2Api.md#delete_iam_v2_ip_group) | **DELETE** /iam/v2/ip-groups/{id} | Delete an IP Group
[**get_iam_v2_ip_group**](IPGroupsIamV2Api.md#get_iam_v2_ip_group) | **GET** /iam/v2/ip-groups/{id} | Read an IP Group
[**list_iam_v2_ip_groups**](IPGroupsIamV2Api.md#list_iam_v2_ip_groups) | **GET** /iam/v2/ip-groups | List of IP Groups
[**update_iam_v2_ip_group**](IPGroupsIamV2Api.md#update_iam_v2_ip_group) | **PATCH** /iam/v2/ip-groups/{id} | Update an IP Group


# **create_iam_v2_ip_group**
> bool, date, datetime, dict, float, int, list, str, none_type create_iam_v2_ip_group()

Create an IP Group

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)  Make a request to create an IP group.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import ip_groups__iam_v2_api
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = ip_groups__iam_v2_api.IPGroupsIamV2Api(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an IP Group
        api_response = api_instance.create_iam_v2_ip_group(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->create_iam_v2_ip_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An IP Group was created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - IpGroup resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iam_v2_ip_group**
> delete_iam_v2_ip_group(id)

Delete an IP Group

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)  Make a request to delete an IP group.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import ip_groups__iam_v2_api
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = ip_groups__iam_v2_api.IPGroupsIamV2Api(api_client)
    id = "id_example" # str | The unique identifier for the IP group.

    # example passing only required values which don't have defaults set
    try:
        # Delete an IP Group
        api_instance.delete_iam_v2_ip_group(id)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->delete_iam_v2_ip_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the IP group. |

### Return type

void (empty response body)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An IP Group is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iam_v2_ip_group**
> bool, date, datetime, dict, float, int, list, str, none_type get_iam_v2_ip_group(id)

Read an IP Group

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)  Make a request to read an IP group.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import ip_groups__iam_v2_api
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = ip_groups__iam_v2_api.IPGroupsIamV2Api(api_client)
    id = "id_example" # str | The unique identifier for the IP group.

    # example passing only required values which don't have defaults set
    try:
        # Read an IP Group
        api_response = api_instance.get_iam_v2_ip_group(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->get_iam_v2_ip_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the IP group. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Group. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_iam_v2_ip_groups**
> bool, date, datetime, dict, float, int, list, str, none_type list_iam_v2_ip_groups()

List of IP Groups

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)  Retrieve a sorted, filtered, paginated list of all IP groups.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import ip_groups__iam_v2_api
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = ip_groups__iam_v2_api.IPGroupsIamV2Api(api_client)
    page_size = 25 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 25
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of IP Groups
        api_response = api_instance.list_iam_v2_ip_groups(page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->list_iam_v2_ip_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| A pagination size for collection requests. | [optional] if omitted the server will use the default value of 25
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Group. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iam_v2_ip_group**
> bool, date, datetime, dict, float, int, list, str, none_type update_iam_v2_ip_group(id)

Update an IP Group

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)  Make a request to update an IP group.  

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import ip_groups__iam_v2_api
from openapi_client.model.iam_v2_ip_group import IamV2IpGroup
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = ip_groups__iam_v2_api.IPGroupsIamV2Api(api_client)
    id = "id_example" # str | The unique identifier for the IP group.
    iam_v2_ip_group = IamV2IpGroup(
        metadata=None,
        group_name="CorpNet",
        cidr_blocks=["192.168.0.0/24","192.168.7.0/24"],
    ) # IamV2IpGroup |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an IP Group
        api_response = api_instance.update_iam_v2_ip_group(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->update_iam_v2_ip_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an IP Group
        api_response = api_instance.update_iam_v2_ip_group(id, iam_v2_ip_group=iam_v2_ip_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IPGroupsIamV2Api->update_iam_v2_ip_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the IP group. |
 **iam_v2_ip_group** | [**IamV2IpGroup**](IamV2IpGroup.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Group. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

