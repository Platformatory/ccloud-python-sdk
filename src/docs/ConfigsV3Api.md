# openapi_client.ConfigsV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_kafka_cluster_config**](ConfigsV3Api.md#delete_kafka_cluster_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Reset Dynamic Broker Config
[**delete_kafka_topic_config**](ConfigsV3Api.md#delete_kafka_topic_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Reset Topic Config
[**get_kafka_cluster_config**](ConfigsV3Api.md#get_kafka_cluster_config) | **GET** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Get Dynamic Broker Config
[**get_kafka_topic_config**](ConfigsV3Api.md#get_kafka_topic_config) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Get Topic Config
[**list_kafka_all_topic_configs**](ConfigsV3Api.md#list_kafka_all_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/-/configs | List All Topic Configs
[**list_kafka_cluster_configs**](ConfigsV3Api.md#list_kafka_cluster_configs) | **GET** /kafka/v3/clusters/{cluster_id}/broker-configs | List Dynamic Broker Configs
[**list_kafka_default_topic_configs**](ConfigsV3Api.md#list_kafka_default_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/default-configs | List New Topic Default Configs
[**list_kafka_topic_configs**](ConfigsV3Api.md#list_kafka_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs | List Topic Configs
[**update_kafka_cluster_config**](ConfigsV3Api.md#update_kafka_cluster_config) | **PUT** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Update Dynamic Broker Config
[**update_kafka_cluster_configs**](ConfigsV3Api.md#update_kafka_cluster_configs) | **POST** /kafka/v3/clusters/{cluster_id}/broker-configs:alter | Batch Alter Dynamic Broker Configs
[**update_kafka_topic_config**](ConfigsV3Api.md#update_kafka_topic_config) | **PUT** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Update Topic Config
[**update_kafka_topic_config_batch**](ConfigsV3Api.md#update_kafka_topic_config_batch) | **POST** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs:alter | Batch Alter Topic Configs


# **delete_kafka_cluster_config**
> delete_kafka_cluster_config(cluster_id, name)

Reset Dynamic Broker Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Reset the configuration parameter specified by ``name`` to its default value by deleting a dynamic cluster-wide configuration.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    name = "compression.type" # str | The configuration parameter name.

    # example passing only required values which don't have defaults set
    try:
        # Reset Dynamic Broker Config
        api_instance.delete_kafka_cluster_config(cluster_id, name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->delete_kafka_cluster_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **name** | **str**| The configuration parameter name. |

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_topic_config**
> delete_kafka_topic_config(cluster_id, topic_name, name)

Reset Topic Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Reset the configuration parameter with given `name` to its default value.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    name = "compression.type" # str | The configuration parameter name.

    # example passing only required values which don't have defaults set
    try:
        # Reset Topic Config
        api_instance.delete_kafka_topic_config(cluster_id, topic_name, name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->delete_kafka_topic_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **name** | **str**| The configuration parameter name. |

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_cluster_config**
> ClusterConfigData get_kafka_cluster_config(cluster_id, name)

Get Dynamic Broker Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the dynamic cluster-wide broker configuration parameter specified by ``name``.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
from openapi_client.model.cluster_config_data import ClusterConfigData
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    name = "compression.type" # str | The configuration parameter name.

    # example passing only required values which don't have defaults set
    try:
        # Get Dynamic Broker Config
        api_response = api_instance.get_kafka_cluster_config(cluster_id, name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->get_kafka_cluster_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **name** | **str**| The configuration parameter name. |

### Return type

[**ClusterConfigData**](ClusterConfigData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cluster configuration parameter. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_topic_config**
> TopicConfigData get_kafka_topic_config(cluster_id, topic_name, name)

Get Topic Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the configuration parameter with the given `name`.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
from openapi_client.model.topic_config_data import TopicConfigData
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    name = "compression.type" # str | The configuration parameter name.

    # example passing only required values which don't have defaults set
    try:
        # Get Topic Config
        api_response = api_instance.get_kafka_topic_config(cluster_id, topic_name, name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->get_kafka_topic_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **name** | **str**| The configuration parameter name. |

### Return type

[**TopicConfigData**](TopicConfigData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The topic configuration parameter. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_all_topic_configs**
> TopicConfigDataList list_kafka_all_topic_configs(cluster_id)

List All Topic Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the list of configuration parameters for all topics hosted by the specified cluster.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.topic_config_data_list import TopicConfigDataList
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # List All Topic Configs
        api_response = api_instance.list_kafka_all_topic_configs(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->list_kafka_all_topic_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**TopicConfigDataList**](TopicConfigDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of cluster configs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_cluster_configs**
> ClusterConfigDataList list_kafka_cluster_configs(cluster_id)

List Dynamic Broker Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return a list of dynamic cluster-wide broker configuration parameters for the specified Kafka cluster. Returns an empty list if there are no dynamic cluster-wide broker configuration parameters.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
from openapi_client.model.cluster_config_data_list import ClusterConfigDataList
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # List Dynamic Broker Configs
        api_response = api_instance.list_kafka_cluster_configs(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->list_kafka_cluster_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**ClusterConfigDataList**](ClusterConfigDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of cluster configs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_default_topic_configs**
> TopicConfigDataList list_kafka_default_topic_configs(cluster_id, topic_name)

List New Topic Default Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  List the default configuration parameters used if the topic were to be newly created.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.topic_config_data_list import TopicConfigDataList
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.

    # example passing only required values which don't have defaults set
    try:
        # List New Topic Default Configs
        api_response = api_instance.list_kafka_default_topic_configs(cluster_id, topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->list_kafka_default_topic_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |

### Return type

[**TopicConfigDataList**](TopicConfigDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of cluster configs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_topic_configs**
> TopicConfigDataList list_kafka_topic_configs(cluster_id, topic_name)

List Topic Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the list of configuration parameters that belong to the specified topic.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.topic_config_data_list import TopicConfigDataList
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.

    # example passing only required values which don't have defaults set
    try:
        # List Topic Configs
        api_response = api_instance.list_kafka_topic_configs(cluster_id, topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->list_kafka_topic_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |

### Return type

[**TopicConfigDataList**](TopicConfigDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of cluster configs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_cluster_config**
> update_kafka_cluster_config(cluster_id, name)

Update Dynamic Broker Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Update the dynamic cluster-wide broker configuration parameter specified by ``name``.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
from openapi_client.model.update_config_request_data import UpdateConfigRequestData
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    name = "compression.type" # str | The configuration parameter name.
    update_config_request_data = UpdateConfigRequestData(
        value="value_example",
    ) # UpdateConfigRequestData | The cluster configuration parameter update request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Dynamic Broker Config
        api_instance.update_kafka_cluster_config(cluster_id, name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_cluster_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Dynamic Broker Config
        api_instance.update_kafka_cluster_config(cluster_id, name, update_config_request_data=update_config_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_cluster_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **name** | **str**| The configuration parameter name. |
 **update_config_request_data** | [**UpdateConfigRequestData**](UpdateConfigRequestData.md)| The cluster configuration parameter update request. | [optional]

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_cluster_configs**
> update_kafka_cluster_configs(cluster_id)

Batch Alter Dynamic Broker Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Update or delete a set of dynamic cluster-wide broker configuration parameters.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.alter_config_batch_request_data import AlterConfigBatchRequestData
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    alter_config_batch_request_data = AlterConfigBatchRequestData(
        data=[
            AlterConfigBatchRequestDataData(
                name="name_example",
                value="value_example",
                operation="operation_example",
            ),
        ],
        validate_only=True,
    ) # AlterConfigBatchRequestData | The alter cluster configuration parameter batch request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Batch Alter Dynamic Broker Configs
        api_instance.update_kafka_cluster_configs(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_cluster_configs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Batch Alter Dynamic Broker Configs
        api_instance.update_kafka_cluster_configs(cluster_id, alter_config_batch_request_data=alter_config_batch_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_cluster_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **alter_config_batch_request_data** | [**AlterConfigBatchRequestData**](AlterConfigBatchRequestData.md)| The alter cluster configuration parameter batch request. | [optional]

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_topic_config**
> update_kafka_topic_config(cluster_id, topic_name, name)

Update Topic Config

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Update the configuration parameter with given `name`.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.error import Error
from openapi_client.model.update_config_request_data import UpdateConfigRequestData
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    name = "compression.type" # str | The configuration parameter name.
    update_config_request_data = UpdateConfigRequestData(
        value="value_example",
    ) # UpdateConfigRequestData | The topic configuration parameter update request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Topic Config
        api_instance.update_kafka_topic_config(cluster_id, topic_name, name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_topic_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Topic Config
        api_instance.update_kafka_topic_config(cluster_id, topic_name, name, update_config_request_data=update_config_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_topic_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **name** | **str**| The configuration parameter name. |
 **update_config_request_data** | [**UpdateConfigRequestData**](UpdateConfigRequestData.md)| The topic configuration parameter update request. | [optional]

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_topic_config_batch**
> update_kafka_topic_config_batch(cluster_id, topic_name)

Batch Alter Topic Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Update or delete a set of topic configuration parameters. Also supports a dry-run mode that only validates whether the operation would succeed if the ``validate_only`` request property is explicitly specified and set to true.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import configs__v3_api
from openapi_client.model.alter_config_batch_request_data import AlterConfigBatchRequestData
from openapi_client.model.error import Error
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
    api_instance = configs__v3_api.ConfigsV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    alter_config_batch_request_data = AlterConfigBatchRequestData(
        data=[
            AlterConfigBatchRequestDataData(
                name="name_example",
                value="value_example",
                operation="operation_example",
            ),
        ],
        validate_only=True,
    ) # AlterConfigBatchRequestData | The alter topic configuration parameter batch request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Batch Alter Topic Configs
        api_instance.update_kafka_topic_config_batch(cluster_id, topic_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_topic_config_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Batch Alter Topic Configs
        api_instance.update_kafka_topic_config_batch(cluster_id, topic_name, alter_config_batch_request_data=alter_config_batch_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigsV3Api->update_kafka_topic_config_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **alter_config_batch_request_data** | [**AlterConfigBatchRequestData**](AlterConfigBatchRequestData.md)| The alter topic configuration parameter batch request. | [optional]

### Return type

void (empty response body)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

