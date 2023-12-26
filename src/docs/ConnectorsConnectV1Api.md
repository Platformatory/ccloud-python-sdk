# openapi_client.ConnectorsConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connectv1_connector**](ConnectorsConnectV1Api.md#create_connectv1_connector) | **POST** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | Create a Connector
[**create_or_update_connectv1_connector_config**](ConnectorsConnectV1Api.md#create_or_update_connectv1_connector_config) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Create or Update a Connector Configuration
[**delete_connectv1_connector**](ConnectorsConnectV1Api.md#delete_connectv1_connector) | **DELETE** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Delete a Connector
[**get_connectv1_connector_config**](ConnectorsConnectV1Api.md#get_connectv1_connector_config) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Read a Connector Configuration
[**list_connectv1_connectors**](ConnectorsConnectV1Api.md#list_connectv1_connectors) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | List of Connectors
[**list_connectv1_connectors_with_expansions**](ConnectorsConnectV1Api.md#list_connectv1_connectors_with_expansions) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors?expand&#x3D;info,status,id | List of Connectors with Expansions
[**read_connectv1_connector**](ConnectorsConnectV1Api.md#read_connectv1_connector) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Read a Connector


# **create_connectv1_connector**
> ConnectV1Connector create_connectv1_connector(environment_id, kafka_cluster_id)

Create a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create a new connector. Returns the new connector information if successful.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.inline_object import InlineObject
from openapi_client.model.connect_v1_connector import ConnectV1Connector
from openapi_client.model.inline_response500 import InlineResponse500
from openapi_client.model.inline_response400 import InlineResponse400
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.
    inline_object = InlineObject(
        name="name_example",
        config={
            "key": "key_example",
        },
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Connector
        api_response = api_instance.create_connectv1_connector(environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->create_connectv1_connector: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Connector
        api_response = api_instance.create_connectv1_connector(environment_id, kafka_cluster_id, inline_object=inline_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->create_connectv1_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_connectv1_connector_config**
> ConnectV1Connector create_or_update_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)

Create or Update a Connector Configuration

Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.connect_v1_connector import ConnectV1Connector
from openapi_client.model.inline_response500 import InlineResponse500
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.
    request_body = {
        "key": "key_example",
    } # {str: (str,)} | Configuration parameters for the connector. All values should be strings. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or Update a Connector Configuration
        api_response = api_instance.create_or_update_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->create_or_update_connectv1_connector_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or Update a Connector Configuration
        api_response = api_instance.create_or_update_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->create_or_update_connectv1_connector_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |
 **request_body** | **{str: (str,)}**| Configuration parameters for the connector. All values should be strings. | [optional]

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connectv1_connector**
> InlineResponse200 delete_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Delete a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a connector. Halts all tasks and deletes the connector configuration.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.inline_response200 import InlineResponse200
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Connector
        api_response = api_instance.delete_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->delete_connectv1_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectv1_connector_config**
> {str: (str,)} get_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)

Read a Connector Configuration

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the configuration for the connector.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # Read a Connector Configuration
        api_response = api_instance.get_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->get_connectv1_connector_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

**{str: (str,)}**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectv1_connectors**
> [str] list_connectv1_connectors(environment_id, kafka_cluster_id)

List of Connectors

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a list of \"names\" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # List of Connectors
        api_response = api_instance.list_connectv1_connectors(environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->list_connectv1_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

**[str]**

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectv1_connectors_with_expansions**
> ConnectV1ConnectorExpansionMap list_connectv1_connectors_with_expansions(environment_id, kafka_cluster_id)

List of Connectors with Expansions

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.connect_v1_connector_expansion_map import ConnectV1ConnectorExpansionMap
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.
    expand = "id" # str | - id : Returns metadata of each connector such as id and id type. - info : Returns metadata of each connector such as the configuration, task information, and type of connector. - status : Returns additional state information of each connector including their status and tasks. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of Connectors with Expansions
        api_response = api_instance.list_connectv1_connectors_with_expansions(environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->list_connectv1_connectors_with_expansions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of Connectors with Expansions
        api_response = api_instance.list_connectv1_connectors_with_expansions(environment_id, kafka_cluster_id, expand=expand)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->list_connectv1_connectors_with_expansions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |
 **expand** | **str**| - id : Returns metadata of each connector such as id and id type. - info : Returns metadata of each connector such as the configuration, task information, and type of connector. - status : Returns additional state information of each connector including their status and tasks. | [optional]

### Return type

[**ConnectV1ConnectorExpansionMap**](ConnectV1ConnectorExpansionMap.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_connectv1_connector**
> ConnectV1Connector read_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Read a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get information about the connector.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import connectors__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.connect_v1_connector import ConnectV1Connector
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

# Configure HTTP basic authorization: cloud-api-key
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
    api_instance = connectors__connect_v1_api.ConnectorsConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # Read a Connector
        api_response = api_instance.read_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectorsConnectV1Api->read_connectv1_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

