# openapi_client.JwksIamV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_iam_v2_json_web_key_set**](JwksIamV2Api.md#refresh_iam_v2_json_web_key_set) | **PATCH** /iam/v2/identity-providers/{provider_id}/jwks | Refresh a provider&#39;s JWKS


# **refresh_iam_v2_json_web_key_set**
> bool, date, datetime, dict, float, int, list, str, none_type refresh_iam_v2_json_web_key_set(provider_id)

Refresh a provider's JWKS

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to refresh the provider's JWKS  

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import jwks__iam_v2_api
from openapi_client.model.iam_v2_jwks import IamV2Jwks
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
    api_instance = jwks__iam_v2_api.JwksIamV2Api(api_client)
    provider_id = "provider_id_example" # str | The Provider
    iam_v2_jwks = IamV2Jwks(
        spec=IamV2JwksSpec(
            jwks_status="REFRESHED",
        ),
    ) # IamV2Jwks |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refresh a provider's JWKS
        api_response = api_instance.refresh_iam_v2_json_web_key_set(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwksIamV2Api->refresh_iam_v2_json_web_key_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refresh a provider's JWKS
        api_response = api_instance.refresh_iam_v2_json_web_key_set(provider_id, iam_v2_jwks=iam_v2_jwks)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwksIamV2Api->refresh_iam_v2_json_web_key_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The Provider |
 **iam_v2_jwks** | [**IamV2Jwks**](IamV2Jwks.md)|  | [optional]

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
**200** | Jwks. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

