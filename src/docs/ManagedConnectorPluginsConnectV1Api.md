# openapi_client.ManagedConnectorPluginsConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_connectv1_connector_plugins**](ManagedConnectorPluginsConnectV1Api.md#list_connectv1_connector_plugins) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connector-plugins | List of Managed Connector plugins
[**validate_connectv1_connector_plugin**](ManagedConnectorPluginsConnectV1Api.md#validate_connectv1_connector_plugin) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connector-plugins/{plugin_name}/config/validate | Validate a Managed Connector Plugin


# **list_connectv1_connector_plugins**
> [InlineResponse2002] list_connectv1_connector_plugins(environment_id, kafka_cluster_id)

List of Managed Connector plugins

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return a list of Managed Connector plugins installed in the Kafka Connect cluster.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import managed_connector_plugins__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = managed_connector_plugins__connect_v1_api.ManagedConnectorPluginsConnectV1Api(api_client)
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # List of Managed Connector plugins
        api_response = api_instance.list_connectv1_connector_plugins(environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ManagedConnectorPluginsConnectV1Api->list_connectv1_connector_plugins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

[**[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector Plugin. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_connectv1_connector_plugin**
> InlineResponse2003 validate_connectv1_connector_plugin(plugin_name, environment_id, kafka_cluster_id)

Validate a Managed Connector Plugin

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import managed_connector_plugins__connect_v1_api
from openapi_client.model.connect_v1_connector_error import ConnectV1ConnectorError
from openapi_client.model.inline_response2003 import InlineResponse2003
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
    api_instance = managed_connector_plugins__connect_v1_api.ManagedConnectorPluginsConnectV1Api(api_client)
    plugin_name = "plugin_name_example" # str | The unique name of the connector plugin.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.
    request_body = {
        "key": "key_example",
    } # {str: (str,)} | Configuration parameters for the connector. All values should be strings. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate a Managed Connector Plugin
        api_response = api_instance.validate_connectv1_connector_plugin(plugin_name, environment_id, kafka_cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ManagedConnectorPluginsConnectV1Api->validate_connectv1_connector_plugin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate a Managed Connector Plugin
        api_response = api_instance.validate_connectv1_connector_plugin(plugin_name, environment_id, kafka_cluster_id, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ManagedConnectorPluginsConnectV1Api->validate_connectv1_connector_plugin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**| The unique name of the connector plugin. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |
 **request_body** | **{str: (str,)}**| Configuration parameters for the connector. All values should be strings. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector Plugin. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

