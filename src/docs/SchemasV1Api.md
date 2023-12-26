# openapi_client.SchemasV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schema**](SchemasV1Api.md#get_schema) | **GET** /schemas/ids/{id} | Get schema string by ID
[**get_schema_only**](SchemasV1Api.md#get_schema_only) | **GET** /schemas/ids/{id}/schema | Get schema by ID
[**get_schema_types**](SchemasV1Api.md#get_schema_types) | **GET** /schemas/types | List supported schema types
[**get_schemas**](SchemasV1Api.md#get_schemas) | **GET** /schemas | List schemas
[**get_subjects**](SchemasV1Api.md#get_subjects) | **GET** /schemas/ids/{id}/subjects | List subjects associated to schema ID
[**get_versions**](SchemasV1Api.md#get_versions) | **GET** /schemas/ids/{id}/versions | List subject-versions associated to schema ID


# **get_schema**
> SchemaString get_schema(id)

Get schema string by ID

Retrieves the schema string identified by the input ID.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.schema_string import SchemaString
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)
    id = 1 # int | Globally unique identifier of the schema
    subject = "subject_example" # str | Name of the subject (optional)
    format = "" # str | Desired output format, dependent on schema type (optional) if omitted the server will use the default value of ""
    fetch_max_id = False # bool | Whether to fetch the maximum schema identifier that exists (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get schema string by ID
        api_response = api_instance.get_schema(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schema: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get schema string by ID
        api_response = api_instance.get_schema(id, subject=subject, format=format, fetch_max_id=fetch_max_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Globally unique identifier of the schema |
 **subject** | **str**| Name of the subject | [optional]
 **format** | **str**| Desired output format, dependent on schema type | [optional] if omitted the server will use the default value of ""
 **fetch_max_id** | **bool**| Whether to fetch the maximum schema identifier that exists | [optional] if omitted the server will use the default value of False

### Return type

[**SchemaString**](SchemaString.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schema string. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40403 indicates schema not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_only**
> str get_schema_only(id)

Get schema by ID

Retrieves the schema identified by the input ID.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)
    id = 1 # int | Globally unique identifier of the schema
    subject = "subject_example" # str | Name of the subject (optional)
    format = "" # str | Desired output format, dependent on schema type (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        # Get schema by ID
        api_response = api_instance.get_schema_only(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schema_only: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get schema by ID
        api_response = api_instance.get_schema_only(id, subject=subject, format=format)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schema_only: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Globally unique identifier of the schema |
 **subject** | **str**| Name of the subject | [optional]
 **format** | **str**| Desired output format, dependent on schema type | [optional] if omitted the server will use the default value of ""

### Return type

**str**

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw schema string. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40403 indicates schema not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_types**
> [str] get_schema_types()

List supported schema types

Retrieve the schema types supported by this registry.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List supported schema types
        api_response = api_instance.get_schema_types()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schema_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported schema types. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas**
> [Schema] get_schemas()

List schemas

Get the schemas matching the specified parameters.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.schema import Schema
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)
    subject_prefix = "" # str | Filters results by the respective subject prefix (optional) if omitted the server will use the default value of ""
    deleted = False # bool | Whether to return soft deleted schemas (optional) if omitted the server will use the default value of False
    latest_only = False # bool | Whether to return latest schema versions only for each matching subject (optional) if omitted the server will use the default value of False
    offset = 0 # int | Pagination offset for results (optional) if omitted the server will use the default value of 0
    limit = -1 # int | Pagination size for results. Ignored if negative (optional) if omitted the server will use the default value of -1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List schemas
        api_response = api_instance.get_schemas(subject_prefix=subject_prefix, deleted=deleted, latest_only=latest_only, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_schemas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_prefix** | **str**| Filters results by the respective subject prefix | [optional] if omitted the server will use the default value of ""
 **deleted** | **bool**| Whether to return soft deleted schemas | [optional] if omitted the server will use the default value of False
 **latest_only** | **bool**| Whether to return latest schema versions only for each matching subject | [optional] if omitted the server will use the default value of False
 **offset** | **int**| Pagination offset for results | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| Pagination size for results. Ignored if negative | [optional] if omitted the server will use the default value of -1

### Return type

[**[Schema]**](Schema.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of schemas matching the specified parameters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subjects**
> [str] get_subjects(id)

List subjects associated to schema ID

Retrieves all the subjects associated with a particular schema ID.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)
    id = 1 # int | Globally unique identifier of the schema
    subject = "subject_example" # str | Filters results by the respective subject (optional)
    deleted = True # bool | Whether to include subjects where the schema was deleted (optional)

    # example passing only required values which don't have defaults set
    try:
        # List subjects associated to schema ID
        api_response = api_instance.get_subjects(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_subjects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List subjects associated to schema ID
        api_response = api_instance.get_subjects(id, subject=subject, deleted=deleted)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_subjects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Globally unique identifier of the schema |
 **subject** | **str**| Filters results by the respective subject | [optional]
 **deleted** | **bool**| Whether to include subjects where the schema was deleted | [optional]

### Return type

**[str]**

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of subjects matching the specified parameters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40403 indicates schema not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> [SubjectVersion] get_versions(id)

List subject-versions associated to schema ID

Get all the subject-version pairs associated with the input ID.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import schemas__v1_api
from openapi_client.model.subject_version import SubjectVersion
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = schemas__v1_api.SchemasV1Api(api_client)
    id = 1 # int | Globally unique identifier of the schema
    subject = "subject_example" # str | Filters results by the respective subject (optional)
    deleted = True # bool | Whether to include subject versions where the schema was deleted (optional)

    # example passing only required values which don't have defaults set
    try:
        # List subject-versions associated to schema ID
        api_response = api_instance.get_versions(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List subject-versions associated to schema ID
        api_response = api_instance.get_versions(id, subject=subject, deleted=deleted)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemasV1Api->get_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Globally unique identifier of the schema |
 **subject** | **str**| Filters results by the respective subject | [optional]
 **deleted** | **bool**| Whether to include subject versions where the schema was deleted | [optional]

### Return type

[**[SubjectVersion]**](SubjectVersion.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of subject versions matching the specified parameters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40403 indicates schema not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

