# openapi_client.ConfigV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subject_config**](ConfigV1Api.md#delete_subject_config) | **DELETE** /config/{subject} | Delete subject compatibility level
[**delete_top_level_config**](ConfigV1Api.md#delete_top_level_config) | **DELETE** /config | Delete global compatibility level
[**get_cluster_config**](ConfigV1Api.md#get_cluster_config) | **GET** /clusterconfig | Get cluster config
[**get_subject_level_config**](ConfigV1Api.md#get_subject_level_config) | **GET** /config/{subject} | Get subject compatibility level
[**get_top_level_config**](ConfigV1Api.md#get_top_level_config) | **GET** /config | Get global compatibility level
[**update_subject_level_config**](ConfigV1Api.md#update_subject_level_config) | **PUT** /config/{subject} | Update subject compatibility level
[**update_top_level_config**](ConfigV1Api.md#update_top_level_config) | **PUT** /config | Update global compatibility level


# **delete_subject_config**
> str delete_subject_config(subject)

Delete subject compatibility level

Deletes the specified subject-level compatibility level config and reverts to the global default.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
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
    api_instance = config__v1_api.ConfigV1Api(api_client)
    subject = "subject_example" # str | Name of the subject

    # example passing only required values which don't have defaults set
    try:
        # Delete subject compatibility level
        api_response = api_instance.delete_subject_config(subject)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->delete_subject_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject |

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
**200** | Operation succeeded. Returns old compatibility level. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_top_level_config**
> str delete_top_level_config()

Delete global compatibility level

Deletes the global compatibility level config and reverts to the default.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
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
    api_instance = config__v1_api.ConfigV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete global compatibility level
        api_response = api_instance.delete_top_level_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->delete_top_level_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Operation succeeded. Returns old global compatibility level. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_config**
> ClusterConfig get_cluster_config()

Get cluster config

Retrieves cluster config information.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
from openapi_client.model.cluster_config import ClusterConfig
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
    api_instance = config__v1_api.ConfigV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster config
        api_response = api_instance.get_cluster_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->get_cluster_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cluster config |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subject_level_config**
> Config get_subject_level_config(subject)

Get subject compatibility level

Retrieves compatibility level, compatibility group, normalization, default metadata, and rule set for a subject.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
from openapi_client.model.config import Config
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
    api_instance = config__v1_api.ConfigV1Api(api_client)
    subject = "subject_example" # str | Name of the subject
    default_to_global = True # bool | Whether to return the global compatibility level  if subject compatibility level not found (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get subject compatibility level
        api_response = api_instance.get_subject_level_config(subject)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->get_subject_level_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get subject compatibility level
        api_response = api_instance.get_subject_level_config(subject, default_to_global=default_to_global)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->get_subject_level_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject |
 **default_to_global** | **bool**| Whether to return the global compatibility level  if subject compatibility level not found | [optional]

### Return type

[**Config**](Config.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subject compatibility level. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_level_config**
> Config get_top_level_config()

Get global compatibility level

Retrieves the global compatibility level, compatibility group, normalization, default metadata, and rule set.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
from openapi_client.model.config import Config
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
    api_instance = config__v1_api.ConfigV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get global compatibility level
        api_response = api_instance.get_top_level_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->get_top_level_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Config**](Config.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The global compatibility level. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subject_level_config**
> ConfigUpdateRequest update_subject_level_config(subject, config_update_request)

Update subject compatibility level

Update compatibility level, compatibility group, normalization, default metadata, and rule set for the specified subject. On success, echoes the original request back to the client.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
from openapi_client.model.config_update_request import ConfigUpdateRequest
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
    api_instance = config__v1_api.ConfigV1Api(api_client)
    subject = "subject_example" # str | Name of the subject
    config_update_request = ConfigUpdateRequest(
        alias="alias_example",
        normalize=True,
        compatibility="FULL_TRANSITIVE",
        compatibility_group="compatibility_group_example",
        default_metadata=ConfigDefaultMetadata(
            properties={},
        ),
        override_metadata=ConfigOverrideMetadata(
            properties={},
        ),
        default_rule_set=ConfigDefaultRuleSet(
            properties={},
        ),
        override_rule_set=ConfigOverrideRuleSet(
            properties={},
        ),
    ) # ConfigUpdateRequest | Config Update Request

    # example passing only required values which don't have defaults set
    try:
        # Update subject compatibility level
        api_response = api_instance.update_subject_level_config(subject, config_update_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->update_subject_level_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject |
 **config_update_request** | [**ConfigUpdateRequest**](ConfigUpdateRequest.md)| Config Update Request |

### Return type

[**ConfigUpdateRequest**](ConfigUpdateRequest.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity. Error code 42203 indicates invalid compatibility level. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. Error code 50003 indicates a failure forwarding the request to the primary. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_level_config**
> ConfigUpdateRequest update_top_level_config(config_update_request)

Update global compatibility level

Updates the global compatibility level, compatibility group, schema normalization, default metadata, and rule set. On success, echoes the original request back to the client.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import config__v1_api
from openapi_client.model.config_update_request import ConfigUpdateRequest
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
    api_instance = config__v1_api.ConfigV1Api(api_client)
    config_update_request = ConfigUpdateRequest(
        alias="alias_example",
        normalize=True,
        compatibility="FULL_TRANSITIVE",
        compatibility_group="compatibility_group_example",
        default_metadata=ConfigDefaultMetadata(
            properties={},
        ),
        override_metadata=ConfigOverrideMetadata(
            properties={},
        ),
        default_rule_set=ConfigDefaultRuleSet(
            properties={},
        ),
        override_rule_set=ConfigOverrideRuleSet(
            properties={},
        ),
    ) # ConfigUpdateRequest | Config Update Request

    # example passing only required values which don't have defaults set
    try:
        # Update global compatibility level
        api_response = api_instance.update_top_level_config(config_update_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigV1Api->update_top_level_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_update_request** | [**ConfigUpdateRequest**](ConfigUpdateRequest.md)| Config Update Request |

### Return type

[**ConfigUpdateRequest**](ConfigUpdateRequest.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity. Error code 42203 indicates invalid compatibility level. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. Error code 50003 indicates a failure forwarding the request to the primary. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

