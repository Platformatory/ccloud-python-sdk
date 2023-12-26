# openapi_client.ConsumerGroupV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kafka_consumer**](ConsumerGroupV3Api.md#get_kafka_consumer) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/consumers/{consumer_id} | Get Consumer
[**get_kafka_consumer_group**](ConsumerGroupV3Api.md#get_kafka_consumer_group) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id} | Get Consumer Group
[**get_kafka_consumer_group_lag_summary**](ConsumerGroupV3Api.md#get_kafka_consumer_group_lag_summary) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lag-summary | Get Consumer Group Lag Summary
[**get_kafka_consumer_lag**](ConsumerGroupV3Api.md#get_kafka_consumer_lag) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lags/{topic_name}/partitions/{partition_id} | Get Consumer Lag
[**list_kafka_consumer_groups**](ConsumerGroupV3Api.md#list_kafka_consumer_groups) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups | List Consumer Groups
[**list_kafka_consumer_lags**](ConsumerGroupV3Api.md#list_kafka_consumer_lags) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lags | List Consumer Lags
[**list_kafka_consumers**](ConsumerGroupV3Api.md#list_kafka_consumers) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/consumers | List Consumers


# **get_kafka_consumer**
> ConsumerData get_kafka_consumer(cluster_id, consumer_group_id, consumer_id)

Get Consumer

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the consumer specified by the ``consumer_id``.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.error import Error
from openapi_client.model.consumer_data import ConsumerData
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.
    consumer_id = "consumer-1" # str | The consumer ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer
        api_response = api_instance.get_kafka_consumer(cluster_id, consumer_group_id, consumer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->get_kafka_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |
 **consumer_id** | **str**| The consumer ID. |

### Return type

[**ConsumerData**](ConsumerData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_consumer_group**
> ConsumerGroupData get_kafka_consumer_group(cluster_id, consumer_group_id)

Get Consumer Group

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the consumer group specified by the ``consumer_group_id``.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.error import Error
from openapi_client.model.consumer_group_data import ConsumerGroupData
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer Group
        api_response = api_instance.get_kafka_consumer_group(cluster_id, consumer_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->get_kafka_consumer_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |

### Return type

[**ConsumerGroupData**](ConsumerGroupData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer group. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_consumer_group_lag_summary**
> ConsumerGroupLagSummaryData get_kafka_consumer_group_lag_summary(cluster_id, consumer_group_id)

Get Consumer Group Lag Summary

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)  Return the maximum and total lag of the consumers belonging to the specified consumer group.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.consumer_group_lag_summary_data import ConsumerGroupLagSummaryData
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer Group Lag Summary
        api_response = api_instance.get_kafka_consumer_group_lag_summary(cluster_id, consumer_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->get_kafka_consumer_group_lag_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |

### Return type

[**ConsumerGroupLagSummaryData**](ConsumerGroupLagSummaryData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The max and total consumer lag in a consumer group. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_consumer_lag**
> ConsumerLagData get_kafka_consumer_lag(cluster_id, consumer_group_id, topic_name, partition_id)

Get Consumer Lag

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)  Return the consumer lag on a partition with the given `partition_id`.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.error import Error
from openapi_client.model.consumer_lag_data import ConsumerLagData
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.
    topic_name = "topic-1" # str | The topic name.
    partition_id = 0 # int | The partition ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Consumer Lag
        api_response = api_instance.get_kafka_consumer_lag(cluster_id, consumer_group_id, topic_name, partition_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->get_kafka_consumer_lag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |
 **topic_name** | **str**| The topic name. |
 **partition_id** | **int**| The partition ID. |

### Return type

[**ConsumerLagData**](ConsumerLagData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer lag. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_consumer_groups**
> ConsumerGroupDataList list_kafka_consumer_groups(cluster_id)

List Consumer Groups

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the list of consumer groups that belong to the specified Kafka cluster.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.consumer_group_data_list import ConsumerGroupDataList
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # List Consumer Groups
        api_response = api_instance.list_kafka_consumer_groups(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->list_kafka_consumer_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**ConsumerGroupDataList**](ConsumerGroupDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of consumer groups. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_consumer_lags**
> ConsumerLagDataList list_kafka_consumer_lags(cluster_id, consumer_group_id)

List Consumer Lags

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)  Return a list of consumer lags of the consumers belonging to the specified consumer group.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.error import Error
from openapi_client.model.consumer_lag_data_list import ConsumerLagDataList
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.

    # example passing only required values which don't have defaults set
    try:
        # List Consumer Lags
        api_response = api_instance.list_kafka_consumer_lags(cluster_id, consumer_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->list_kafka_consumer_lags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |

### Return type

[**ConsumerLagDataList**](ConsumerLagDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of consumer lags. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_consumers**
> ConsumerDataList list_kafka_consumers(cluster_id, consumer_group_id)

List Consumers

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return a list of consumers that belong to the specified consumer group.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import consumer_group__v3_api
from openapi_client.model.error import Error
from openapi_client.model.consumer_data_list import ConsumerDataList
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
    api_instance = consumer_group__v3_api.ConsumerGroupV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    consumer_group_id = "consumer-group-1" # str | The consumer group ID.

    # example passing only required values which don't have defaults set
    try:
        # List Consumers
        api_response = api_instance.list_kafka_consumers(cluster_id, consumer_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsumerGroupV3Api->list_kafka_consumers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **consumer_group_id** | **str**| The consumer group ID. |

### Return type

[**ConsumerDataList**](ConsumerDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of consumers. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

