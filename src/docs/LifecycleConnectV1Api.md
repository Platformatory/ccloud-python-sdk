# openapi_client.LifecycleConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pause_connectv1_connector**](LifecycleConnectV1Api.md#pause_connectv1_connector) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/pause | Pause a Connector
[**resume_connectv1_connector**](LifecycleConnectV1Api.md#resume_connectv1_connector) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/resume | Resume a Connector


# **pause_connectv1_connector**
> pause_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Pause a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Pause the connector and its tasks. Stops message processing until the connector is resumed. This call is asynchronous and the tasks will not transition to PAUSED state at the same time.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import lifecycle__connect_v1_api
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
    api_instance = lifecycle__connect_v1_api.LifecycleConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # Pause a Connector
        api_instance.pause_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling LifecycleConnectV1Api->pause_connectv1_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

void (empty response body)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_connectv1_connector**
> resume_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Resume a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Resume a paused connector or do nothing if the connector is not paused. This call is asynchronous and the tasks will not transition to RUNNING state at the same time.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):

```python
import time
import openapi_client
from openapi_client.api import lifecycle__connect_v1_api
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
    api_instance = lifecycle__connect_v1_api.LifecycleConnectV1Api(api_client)
    connector_name = "connector_name_example" # str | The unique name of the connector.
    environment_id = "environment_id_example" # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = "kafka_cluster_id_example" # str | The unique identifier for the Kafka cluster.

    # example passing only required values which don't have defaults set
    try:
        # Resume a Connector
        api_instance.resume_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling LifecycleConnectV1Api->resume_connectv1_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. |
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. |
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. |

### Return type

void (empty response body)

### Authorization

[cloud-api-key](../README.md#cloud-api-key), [confluent-sts-access-token](../README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

