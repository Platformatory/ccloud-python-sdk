# openapi_client.StatementExceptionsSqlV1beta1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sqlv1beta1_statement_exceptions**](StatementExceptionsSqlV1beta1Api.md#get_sqlv1beta1_statement_exceptions) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name}/exceptions | List of Statement Exceptions


# **get_sqlv1beta1_statement_exceptions**
> SqlV1beta1StatementExceptionList get_sqlv1beta1_statement_exceptions(organization_id, environment_id, statement_name)

List of Statement Exceptions

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a list of the 10 most recent statement exceptions.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statement_exceptions__sql_v1beta1_api
from openapi_client.model.sql_v1beta1_statement_exception_list import SqlV1beta1StatementExceptionList
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

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = statement_exceptions__sql_v1beta1_api.StatementExceptionsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    statement_name = "statement_name_example" # str | The unique identifier for the statement.

    # example passing only required values which don't have defaults set
    try:
        # List of Statement Exceptions
        api_response = api_instance.get_sqlv1beta1_statement_exceptions(organization_id, environment_id, statement_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementExceptionsSqlV1beta1Api->get_sqlv1beta1_statement_exceptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **statement_name** | **str**| The unique identifier for the statement. |

### Return type

[**SqlV1beta1StatementExceptionList**](SqlV1beta1StatementExceptionList.md)

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statement Exceptions. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

