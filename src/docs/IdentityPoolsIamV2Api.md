# openapi_client.IdentityPoolsIamV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iam_v2_identity_pool**](IdentityPoolsIamV2Api.md#create_iam_v2_identity_pool) | **POST** /iam/v2/identity-providers/{provider_id}/identity-pools | Create an Identity Pool
[**delete_iam_v2_identity_pool**](IdentityPoolsIamV2Api.md#delete_iam_v2_identity_pool) | **DELETE** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Delete an Identity Pool
[**get_iam_v2_identity_pool**](IdentityPoolsIamV2Api.md#get_iam_v2_identity_pool) | **GET** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Read an Identity Pool
[**list_iam_v2_identity_pools**](IdentityPoolsIamV2Api.md#list_iam_v2_identity_pools) | **GET** /iam/v2/identity-providers/{provider_id}/identity-pools | List of Identity Pools
[**update_iam_v2_identity_pool**](IdentityPoolsIamV2Api.md#update_iam_v2_identity_pool) | **PATCH** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Update an Identity Pool


# **create_iam_v2_identity_pool**
> bool, date, datetime, dict, float, int, list, str, none_type create_iam_v2_identity_pool(provider_id)

Create an Identity Pool

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create an identity pool.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import identity_pools__iam_v2_api
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
    api_instance = identity_pools__iam_v2_api.IdentityPoolsIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an Identity Pool
        api_response = api_instance.create_iam_v2_identity_pool(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->create_iam_v2_identity_pool: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Identity Pool
        api_response = api_instance.create_iam_v2_identity_pool(provider_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->create_iam_v2_identity_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
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
**201** | An Identity Pool was created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - IdentityPool resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iam_v2_identity_pool**
> delete_iam_v2_identity_pool(provider_id, id)

Delete an Identity Pool

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete an identity pool.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import identity_pools__iam_v2_api
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
    api_instance = identity_pools__iam_v2_api.IdentityPoolsIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    id = "id_example" # str | The unique identifier for the identity pool.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Identity Pool
        api_instance.delete_iam_v2_identity_pool(provider_id, id)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->delete_iam_v2_identity_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
 **id** | **str**| The unique identifier for the identity pool. |

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
**204** | An Identity Pool is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iam_v2_identity_pool**
> bool, date, datetime, dict, float, int, list, str, none_type get_iam_v2_identity_pool(provider_id, id)

Read an Identity Pool

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read an identity pool.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import identity_pools__iam_v2_api
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
    api_instance = identity_pools__iam_v2_api.IdentityPoolsIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    id = "id_example" # str | The unique identifier for the identity pool.

    # example passing only required values which don't have defaults set
    try:
        # Read an Identity Pool
        api_response = api_instance.get_iam_v2_identity_pool(provider_id, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->get_iam_v2_identity_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
 **id** | **str**| The unique identifier for the identity pool. |

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
**200** | Identity Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_iam_v2_identity_pools**
> bool, date, datetime, dict, float, int, list, str, none_type list_iam_v2_identity_pools(provider_id)

List of Identity Pools

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all identity pools.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import identity_pools__iam_v2_api
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
    api_instance = identity_pools__iam_v2_api.IdentityPoolsIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    page_size = 10 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 10
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of Identity Pools
        api_response = api_instance.list_iam_v2_identity_pools(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->list_iam_v2_identity_pools: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Identity Pools
        api_response = api_instance.list_iam_v2_identity_pools(provider_id, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->list_iam_v2_identity_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
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
**200** | Identity Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iam_v2_identity_pool**
> bool, date, datetime, dict, float, int, list, str, none_type update_iam_v2_identity_pool(provider_id, id)

Update an Identity Pool

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update an identity pool.  

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import identity_pools__iam_v2_api
from openapi_client.model.failure import Failure
from openapi_client.model.iam_v2_identity_pool import IamV2IdentityPool
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
    api_instance = identity_pools__iam_v2_api.IdentityPoolsIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    id = "id_example" # str | The unique identifier for the identity pool.
    iam_v2_identity_pool = IamV2IdentityPool(
        metadata=None,
        display_name="My Identity Pool",
        description="Prod Access to Kafka clusters to Release Engineering",
        identity_claim="claims.sub",
        filter="claims.aud=="confluent" && claims.group!="invalid_group"",
    ) # IamV2IdentityPool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Identity Pool
        api_response = api_instance.update_iam_v2_identity_pool(provider_id, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->update_iam_v2_identity_pool: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Identity Pool
        api_response = api_instance.update_iam_v2_identity_pool(provider_id, id, iam_v2_identity_pool=iam_v2_identity_pool)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityPoolsIamV2Api->update_iam_v2_identity_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
 **id** | **str**| The unique identifier for the identity pool. |
 **iam_v2_identity_pool** | [**IamV2IdentityPool**](IamV2IdentityPool.md)|  | [optional]

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
**200** | Identity Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

