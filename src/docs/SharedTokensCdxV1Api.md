# openapi_client.SharedTokensCdxV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_cdx_v1_shared_token**](SharedTokensCdxV1Api.md#redeem_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:redeem | Redeem token
[**resources_cdx_v1_shared_token**](SharedTokensCdxV1Api.md#resources_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:resources | Validate token to view shared resources


# **redeem_cdx_v1_shared_token**
> CdxV1RedeemTokenResponse redeem_cdx_v1_shared_token()

Redeem token

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Redeem the shared token for shared topic and cluster access information

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import shared_tokens__cdx_v1_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.cdx_v1_redeem_token_response import CdxV1RedeemTokenResponse
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
    api_instance = shared_tokens__cdx_v1_api.SharedTokensCdxV1Api(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Redeem token
        api_response = api_instance.redeem_cdx_v1_shared_token(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SharedTokensCdxV1Api->redeem_cdx_v1_shared_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**CdxV1RedeemTokenResponse**](CdxV1RedeemTokenResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer redeems shared token  |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_cdx_v1_shared_token**
> InlineResponse2005 resources_cdx_v1_shared_token()

Validate token to view shared resources

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Validate and decrypt the shared token and view token's shared resources

### Example

* Basic Authentication (api-key):

```python
import time
import openapi_client
from openapi_client.api import shared_tokens__cdx_v1_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.inline_response2005 import InlineResponse2005
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
    api_instance = shared_tokens__cdx_v1_api.SharedTokensCdxV1Api(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate token to view shared resources
        api_response = api_instance.resources_cdx_v1_shared_token(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SharedTokensCdxV1Api->resources_cdx_v1_shared_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer validates share token and view consumer resources before redeeming in the workflow  |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

