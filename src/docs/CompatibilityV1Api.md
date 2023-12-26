# openapi_client.CompatibilityV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_compatibility_by_subject_name**](CompatibilityV1Api.md#test_compatibility_by_subject_name) | **POST** /compatibility/subjects/{subject}/versions/{version} | Test schema compatibility against a particular schema subject-version
[**test_compatibility_for_subject**](CompatibilityV1Api.md#test_compatibility_for_subject) | **POST** /compatibility/subjects/{subject}/versions | Test schema compatibility against all schemas under a subject


# **test_compatibility_by_subject_name**
> CompatibilityCheckResponse test_compatibility_by_subject_name(subject, version, register_schema_request)

Test schema compatibility against a particular schema subject-version

Test input schema against a particular version of a subject's schema for compatibility. The compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import compatibility__v1_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.compatibility_check_response import CompatibilityCheckResponse
from openapi_client.model.register_schema_request import RegisterSchemaRequest
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

# Configure OAuth2 access token for authorization: external-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compatibility__v1_api.CompatibilityV1Api(api_client)
    subject = "subject_example" # str | Subject of the schema version against which compatibility is to be tested
    version = "version_example" # str | Version of the subject's schema against which compatibility is to be tested. Valid values for versionId are between [1,2^31-1] or the string \"latest\".\"latest\" checks compatibility of the input schema with the last registered schema under the specified subject
    register_schema_request = RegisterSchemaRequest(
        version=1,
        id=1,
        schema_type="schema_type_example",
        references=[
            SchemaReference(
                name="io.confluent.kafka.example.User",
                subject="User",
                version=1,
            ),
        ],
        schema="schema_example",
    ) # RegisterSchemaRequest | Schema
    verbose = True # bool | Whether to return detailed error messages (optional)

    # example passing only required values which don't have defaults set
    try:
        # Test schema compatibility against a particular schema subject-version
        api_response = api_instance.test_compatibility_by_subject_name(subject, version, register_schema_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompatibilityV1Api->test_compatibility_by_subject_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test schema compatibility against a particular schema subject-version
        api_response = api_instance.test_compatibility_by_subject_name(subject, version, register_schema_request, verbose=verbose)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompatibilityV1Api->test_compatibility_by_subject_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Subject of the schema version against which compatibility is to be tested |
 **version** | **str**| Version of the subject&#39;s schema against which compatibility is to be tested. Valid values for versionId are between [1,2^31-1] or the string \&quot;latest\&quot;.\&quot;latest\&quot; checks compatibility of the input schema with the last registered schema under the specified subject |
 **register_schema_request** | [**RegisterSchemaRequest**](RegisterSchemaRequest.md)| Schema |
 **verbose** | **bool**| Whether to return detailed error messages | [optional]

### Return type

[**CompatibilityCheckResponse**](CompatibilityCheckResponse.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compatibility check result. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40402 indicates version not found. |  -  |
**422** | Unprocessable entity. Error code 42201 indicates an invalid schema or schema type. Error code 42202 indicates an invalid version. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_compatibility_for_subject**
> CompatibilityCheckResponse test_compatibility_for_subject(subject, register_schema_request)

Test schema compatibility against all schemas under a subject

Test input schema against a subject's schemas for compatibility, based on the configured compatibility level of the subject. In other words, it will perform the same compatibility check as register for that subject. The compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import compatibility__v1_api
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.compatibility_check_response import CompatibilityCheckResponse
from openapi_client.model.register_schema_request import RegisterSchemaRequest
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

# Configure OAuth2 access token for authorization: external-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compatibility__v1_api.CompatibilityV1Api(api_client)
    subject = "subject_example" # str | Subject of the schema version against which compatibility is to be tested
    register_schema_request = RegisterSchemaRequest(
        version=1,
        id=1,
        schema_type="schema_type_example",
        references=[
            SchemaReference(
                name="io.confluent.kafka.example.User",
                subject="User",
                version=1,
            ),
        ],
        schema="schema_example",
    ) # RegisterSchemaRequest | Schema
    verbose = True # bool | Whether to return detailed error messages (optional)

    # example passing only required values which don't have defaults set
    try:
        # Test schema compatibility against all schemas under a subject
        api_response = api_instance.test_compatibility_for_subject(subject, register_schema_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompatibilityV1Api->test_compatibility_for_subject: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test schema compatibility against all schemas under a subject
        api_response = api_instance.test_compatibility_for_subject(subject, register_schema_request, verbose=verbose)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompatibilityV1Api->test_compatibility_for_subject: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Subject of the schema version against which compatibility is to be tested |
 **register_schema_request** | [**RegisterSchemaRequest**](RegisterSchemaRequest.md)| Schema |
 **verbose** | **bool**| Whether to return detailed error messages | [optional]

### Return type

[**CompatibilityCheckResponse**](CompatibilityCheckResponse.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compatibility check result. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

