# openapi_client.StatementsSqlV1beta1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sqlv1beta1_statement**](StatementsSqlV1beta1Api.md#create_sqlv1beta1_statement) | **POST** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements | Create a Statement
[**delete_sqlv1beta1_statement**](StatementsSqlV1beta1Api.md#delete_sqlv1beta1_statement) | **DELETE** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Delete a Statement
[**get_sqlv1beta1_statement**](StatementsSqlV1beta1Api.md#get_sqlv1beta1_statement) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Read a Statement
[**list_sqlv1beta1_statements**](StatementsSqlV1beta1Api.md#list_sqlv1beta1_statements) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements | List of Statements
[**update_sqlv1beta1_statement**](StatementsSqlV1beta1Api.md#update_sqlv1beta1_statement) | **PUT** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Update a Statement


# **create_sqlv1beta1_statement**
> bool, date, datetime, dict, float, int, list, str, none_type create_sqlv1beta1_statement(organization_id, environment_id)

Create a Statement

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a statement.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statements__sql_v1beta1_api
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

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = statements__sql_v1beta1_api.StatementsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Statement
        api_response = api_instance.create_sqlv1beta1_statement(organization_id, environment_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->create_sqlv1beta1_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Statement
        api_response = api_instance.create_sqlv1beta1_statement(organization_id, environment_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->create_sqlv1beta1_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Statement is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Statement resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sqlv1beta1_statement**
> delete_sqlv1beta1_statement(organization_id, environment_id, statement_name)

Delete a Statement

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a statement.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statements__sql_v1beta1_api
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
    api_instance = statements__sql_v1beta1_api.StatementsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    statement_name = "statement_name_example" # str | The unique identifier for the statement.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Statement
        api_instance.delete_sqlv1beta1_statement(organization_id, environment_id, statement_name)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->delete_sqlv1beta1_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **statement_name** | **str**| The unique identifier for the statement. |

### Return type

void (empty response body)

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Statement is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sqlv1beta1_statement**
> bool, date, datetime, dict, float, int, list, str, none_type get_sqlv1beta1_statement(organization_id, environment_id, statement_name)

Read a Statement

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a statement.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statements__sql_v1beta1_api
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
    api_instance = statements__sql_v1beta1_api.StatementsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    statement_name = "statement_name_example" # str | The unique identifier for the statement.

    # example passing only required values which don't have defaults set
    try:
        # Read a Statement
        api_response = api_instance.get_sqlv1beta1_statement(organization_id, environment_id, statement_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->get_sqlv1beta1_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **statement_name** | **str**| The unique identifier for the statement. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statement. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sqlv1beta1_statements**
> SqlV1beta1StatementList list_sqlv1beta1_statements(organization_id, environment_id)

List of Statements

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all statements.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statements__sql_v1beta1_api
from openapi_client.model.failure import Failure
from openapi_client.model.sql_v1beta1_statement_list import SqlV1beta1StatementList
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
    api_instance = statements__sql_v1beta1_api.StatementsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    spec_compute_pool_id = "lfcp-00000" # str | Filter the results by exact match for spec.compute_pool. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) if omitted the server will use the default value of 10
    page_token = "page_token_example" # str | An opaque pagination token for collection requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of Statements
        api_response = api_instance.list_sqlv1beta1_statements(organization_id, environment_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->list_sqlv1beta1_statements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Statements
        api_response = api_instance.list_sqlv1beta1_statements(organization_id, environment_id, spec_compute_pool_id=spec_compute_pool_id, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->list_sqlv1beta1_statements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **spec_compute_pool_id** | **str**| Filter the results by exact match for spec.compute_pool. | [optional]
 **page_size** | **int**| A pagination size for collection requests. | [optional] if omitted the server will use the default value of 10
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional]

### Return type

[**SqlV1beta1StatementList**](SqlV1beta1StatementList.md)

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statements. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sqlv1beta1_statement**
> update_sqlv1beta1_statement(organization_id, environment_id, statement_name)

Update a Statement

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a statement.

### Example

* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import statements__sql_v1beta1_api
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

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = statements__sql_v1beta1_api.StatementsSqlV1beta1Api(api_client)
    organization_id = "organization_id_example" # str | The unique identifier for the organization.
    environment_id = "environment_id_example" # str | The unique identifier for the environment.
    statement_name = "statement_name_example" # str | The unique identifier for the statement.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Statement
        api_instance.update_sqlv1beta1_statement(organization_id, environment_id, statement_name)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->update_sqlv1beta1_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Statement
        api_instance.update_sqlv1beta1_statement(organization_id, environment_id, statement_name, unknown_base_type=unknown_base_type)
    except openapi_client.ApiException as e:
        print("Exception when calling StatementsSqlV1beta1Api->update_sqlv1beta1_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The unique identifier for the organization. |
 **environment_id** | **str**| The unique identifier for the environment. |
 **statement_name** | **str**| The unique identifier for the statement. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Statement is being updated. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

