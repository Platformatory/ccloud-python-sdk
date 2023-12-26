# openapi_client.SignupPartnerV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_signup**](SignupPartnerV2Api.md#activate_signup) | **POST** /partner/v2/signup/activate | Activate an Incomplete Signup
[**signup**](SignupPartnerV2Api.md#signup) | **POST** /partner/v2/signup | Signup an Organization on behalf of a Customer
[**signup_partner_v2_link**](SignupPartnerV2Api.md#signup_partner_v2_link) | **POST** /partner/v2/signup/link | Signup a Customer by Linking to an Existing Organization


# **activate_signup**
> PartnerSignupResponse activate_signup()

Activate an Incomplete Signup

[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)  Creates a user in the organization previously created in `/partner/v2/signup`. This completes the signup process if you did not pass in user details to `/partner/v2/signup`. Calling this endpoint if the signup  process has been completed will result in a `409 Conflict` error.

### Example

* OAuth Authentication (oauth):

```python
import time
import openapi_client
from openapi_client.api import signup__partner_v2_api
from openapi_client.model.partner_signup_response import PartnerSignupResponse
from openapi_client.model.failure import Failure
from openapi_client.model.activate_partner_signup_request import ActivatePartnerSignupRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signup__partner_v2_api.SignupPartnerV2Api(api_client)
    activate_partner_signup_request = ActivatePartnerSignupRequest(
        user=None,
        organization_id="b3a17773-05cc-4431-9560-433fb4613da8",
    ) # ActivatePartnerSignupRequest | A JSON object containing signup information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activate an Incomplete Signup
        api_response = api_instance.activate_signup(activate_partner_signup_request=activate_partner_signup_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignupPartnerV2Api->activate_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_partner_signup_request** | [**ActivatePartnerSignupRequest**](ActivatePartnerSignupRequest.md)| A JSON object containing signup information | [optional]

### Return type

[**PartnerSignupResponse**](PartnerSignupResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful signup activation. User is being created. |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup**
> PartnerSignupResponse signup()

Signup an Organization on behalf of a Customer

[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)  Create an organization for a customer. You must pass in either an entitlement object reference (a url to  a previously created entitlement) or entitlement details. If you pass in an entitlement object reference, we will link with the  created entitlement. If you pass in the entitlement details, we will create the entitlement with the organization  in a single transaction. If you pass in user details (email, given name, and family name), we will create a user as well. If you do not pass in user details, you MUST call `/partner/v2/signup/activate` with user details to complete signup.

### Example

* OAuth Authentication (oauth):

```python
import time
import openapi_client
from openapi_client.api import signup__partner_v2_api
from openapi_client.model.partner_signup_request import PartnerSignupRequest
from openapi_client.model.partner_signup_response import PartnerSignupResponse
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

# Configure OAuth2 access token for authorization: oauth
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signup__partner_v2_api.SignupPartnerV2Api(api_client)
    dry_run = True # bool | If true, only perform validation of signup (optional)
    partner_signup_request = PartnerSignupRequest(
        organization=None,
        user=None,
        entitlement=None,
    ) # PartnerSignupRequest | A JSON object containing signup information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Signup an Organization on behalf of a Customer
        api_response = api_instance.signup(dry_run=dry_run, partner_signup_request=partner_signup_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignupPartnerV2Api->signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dry_run** | **bool**| If true, only perform validation of signup | [optional]
 **partner_signup_request** | [**PartnerSignupRequest**](PartnerSignupRequest.md)| A JSON object containing signup information | [optional]

### Return type

[**PartnerSignupResponse**](PartnerSignupResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful signup. |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_partner_v2_link**
> PartnerSignupResponse signup_partner_v2_link()

Signup a Customer by Linking to an Existing Organization

[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)  Signup a customer by linking a new entitlement to an existing Confluent Cloud organization.

### Example

* OAuth Authentication (oauth):

```python
import time
import openapi_client
from openapi_client.api import signup__partner_v2_api
from openapi_client.model.partner_signup_response import PartnerSignupResponse
from openapi_client.model.failure import Failure
from openapi_client.model.partner_link_request import PartnerLinkRequest
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

# Configure OAuth2 access token for authorization: oauth
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signup__partner_v2_api.SignupPartnerV2Api(api_client)
    dry_run = True # bool | If true, only perform validation of signup (optional)
    partner_link_request = PartnerLinkRequest(
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
        organization=None,
        entitlement=None,
    ) # PartnerLinkRequest | A JSON object containing signup information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Signup a Customer by Linking to an Existing Organization
        api_response = api_instance.signup_partner_v2_link(dry_run=dry_run, partner_link_request=partner_link_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignupPartnerV2Api->signup_partner_v2_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dry_run** | **bool**| If true, only perform validation of signup | [optional]
 **partner_link_request** | [**PartnerLinkRequest**](PartnerLinkRequest.md)| A JSON object containing signup information | [optional]

### Return type

[**PartnerSignupResponse**](PartnerSignupResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful signup. |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

