# openapi_client.OAuthTokensStsV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_sts_v1_oauth_token**](OAuthTokensStsV1Api.md#exchange_sts_v1_oauth_token) | **POST** /sts/v1/oauth2/token | Exchange an OAuth Token


# **exchange_sts_v1_oauth_token**
> StsV1TokenExchangeReply exchange_sts_v1_oauth_token()

Exchange an OAuth Token

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Use this operation to exchange an access token (JWT) issued by an external identity provider for an access token (JWT) issued by Confluent.This enables the use of external identities to access Confluent Cloud APIs. 

### Example


```python
import time
import openapi_client
from openapi_client.api import o_auth_tokens__sts_v1_api
from openapi_client.model.sts_v1_token_exchange_reply import StsV1TokenExchangeReply
from openapi_client.model.failure import Failure
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = o_auth_tokens__sts_v1_api.OAuthTokensStsV1Api(api_client)
    api_version = "sts/v1" # str | APIVersion defines the schema version of this representation of a resource. (optional) if omitted the server will use the default value of "sts/v1"
    kind = "TokenExchangeRequest" # str | Kind defines the object this REST resource represents. (optional) if omitted the server will use the default value of "TokenExchangeRequest"
    id = "dlz-f3a90de" # str | ID is the \\\"natural identifier\\\" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\\\"time\\\"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace (\\\"space\\\"). (optional)
    metadata = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    grant_type = "urn:ietf:params:oauth:grant-type:token-exchange" # str | The grant type. Must be urn:ietf:params:oauth:grant-type:token-exchange, which indicates a token exchange.  (optional)
    subject_token = "test_jwt_token" # str | Confluent Cloud only accepts JSON Web Token (JWT) access tokens from customer identity provider (optional)
    identity_pool_id = "pool_1" # str | Identity pool is a group of external identities that are assigned a certain level of access based on policy  (optional)
    subject_token_type = "urn:ietf:params:oauth:token-type:jwt" # str | An identifier for the type of requested security token. Supported values is urn:ietf:params:oauth:token-type:jwt.  (optional)
    requested_token_type = "urn:ietf:params:oauth:token-type:access_token" # str | An identifier for the type of requested security token. Supported values is urn:ietf:params:oauth:token-type:access_token.  (optional)
    expires_in = 900 # int | The amount of time, in seconds, between the time when the access token was issued and the time when the access token will expire  (optional) if omitted the server will use the default value of 900

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exchange an OAuth Token
        api_response = api_instance.exchange_sts_v1_oauth_token(api_version=api_version, kind=kind, id=id, metadata=metadata, grant_type=grant_type, subject_token=subject_token, identity_pool_id=identity_pool_id, subject_token_type=subject_token_type, requested_token_type=requested_token_type, expires_in=expires_in)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OAuthTokensStsV1Api->exchange_sts_v1_oauth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| APIVersion defines the schema version of this representation of a resource. | [optional] if omitted the server will use the default value of "sts/v1"
 **kind** | **str**| Kind defines the object this REST resource represents. | [optional] if omitted the server will use the default value of "TokenExchangeRequest"
 **id** | **str**| ID is the \\\&quot;natural identifier\\\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\\\&quot;time\\\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\\\&quot;space\\\&quot;). | [optional]
 **metadata** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **grant_type** | **str**| The grant type. Must be urn:ietf:params:oauth:grant-type:token-exchange, which indicates a token exchange.  | [optional]
 **subject_token** | **str**| Confluent Cloud only accepts JSON Web Token (JWT) access tokens from customer identity provider | [optional]
 **identity_pool_id** | **str**| Identity pool is a group of external identities that are assigned a certain level of access based on policy  | [optional]
 **subject_token_type** | **str**| An identifier for the type of requested security token. Supported values is urn:ietf:params:oauth:token-type:jwt.  | [optional]
 **requested_token_type** | **str**| An identifier for the type of requested security token. Supported values is urn:ietf:params:oauth:token-type:access_token.  | [optional]
 **expires_in** | **int**| The amount of time, in seconds, between the time when the access token was issued and the time when the access token will expire  | [optional] if omitted the server will use the default value of 900

### Return type

[**StsV1TokenExchangeReply**](StsV1TokenExchangeReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access token used to access public control plane api  |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

