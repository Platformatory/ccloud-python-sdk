# openapi_client.TopicV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kafka_topic**](TopicV3Api.md#create_kafka_topic) | **POST** /kafka/v3/clusters/{cluster_id}/topics | Create Topic
[**delete_kafka_topic**](TopicV3Api.md#delete_kafka_topic) | **DELETE** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Delete Topic
[**get_kafka_topic**](TopicV3Api.md#get_kafka_topic) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Get Topic
[**list_kafka_topics**](TopicV3Api.md#list_kafka_topics) | **GET** /kafka/v3/clusters/{cluster_id}/topics | List Topics
[**update_partition_count_kafka_topic**](TopicV3Api.md#update_partition_count_kafka_topic) | **PATCH** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Update Partition Count


# **create_kafka_topic**
> TopicData create_kafka_topic(cluster_id)

Create Topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create a topic. Also supports a dry-run mode that only validates whether the topic creation would succeed if the ``validate_only`` request property is explicitly specified and set to true. Note that when dry-run mode is being used the response status would be 200 OK instead of 201 Created.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import topic__v3_api
from openapi_client.model.error import Error
from openapi_client.model.create_topic_request_data import CreateTopicRequestData
from openapi_client.model.topic_data import TopicData
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
    api_instance = topic__v3_api.TopicV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    create_topic_request_data = CreateTopicRequestData(
        topic_name="topic_name_example",
        partitions_count=1,
        replication_factor=1,
        configs=[
            CreateTopicRequestDataConfigs(
                name="name_example",
                value="value_example",
            ),
        ],
        validate_only=True,
    ) # CreateTopicRequestData | The topic creation request. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Topic
        api_response = api_instance.create_kafka_topic(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->create_kafka_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Topic
        api_response = api_instance.create_kafka_topic(cluster_id, create_topic_request_data=create_topic_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->create_kafka_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **create_topic_request_data** | [**CreateTopicRequestData**](CreateTopicRequestData.md)| The topic creation request. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). | [optional]

### Return type

[**TopicData**](TopicData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created topic. |  -  |
**201** | The created topic. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_topic**
> delete_kafka_topic(cluster_id, topic_name)

Delete Topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete the topic with the given `topic_name`.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import topic__v3_api
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
    api_instance = topic__v3_api.TopicV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.

    # example passing only required values which don't have defaults set
    try:
        # Delete Topic
        api_instance.delete_kafka_topic(cluster_id, topic_name)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->delete_kafka_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |

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

# **get_kafka_topic**
> TopicData get_kafka_topic(cluster_id, topic_name)

Get Topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the topic with the given `topic_name`.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import topic__v3_api
from openapi_client.model.error import Error
from openapi_client.model.topic_data import TopicData
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
    api_instance = topic__v3_api.TopicV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    include_authorized_operations = True # bool | Specify if authorized operations should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Topic
        api_response = api_instance.get_kafka_topic(cluster_id, topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->get_kafka_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Topic
        api_response = api_instance.get_kafka_topic(cluster_id, topic_name, include_authorized_operations=include_authorized_operations)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->get_kafka_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **include_authorized_operations** | **bool**| Specify if authorized operations should be included in the response. | [optional]

### Return type

[**TopicData**](TopicData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The topic. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_topics**
> TopicDataList list_kafka_topics(cluster_id)

List Topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the list of topics that belong to the specified Kafka cluster.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import topic__v3_api
from openapi_client.model.topic_data_list import TopicDataList
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
    api_instance = topic__v3_api.TopicV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # List Topics
        api_response = api_instance.list_kafka_topics(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->list_kafka_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**TopicDataList**](TopicDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of topics. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_partition_count_kafka_topic**
> TopicData update_partition_count_kafka_topic(cluster_id, topic_name)

Update Partition Count

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Increase the number of partitions for a topic.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import topic__v3_api
from openapi_client.model.update_partition_count_request_data import UpdatePartitionCountRequestData
from openapi_client.model.error import Error
from openapi_client.model.topic_data import TopicData
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
    api_instance = topic__v3_api.TopicV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    topic_name = "topic-1" # str | The topic name.
    update_partition_count_request_data = UpdatePartitionCountRequestData(
        partitions_count=1,
    ) # UpdatePartitionCountRequestData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Partition Count
        api_response = api_instance.update_partition_count_kafka_topic(cluster_id, topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->update_partition_count_kafka_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Partition Count
        api_response = api_instance.update_partition_count_kafka_topic(cluster_id, topic_name, update_partition_count_request_data=update_partition_count_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicV3Api->update_partition_count_kafka_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **topic_name** | **str**| The topic name. |
 **update_partition_count_request_data** | [**UpdatePartitionCountRequestData**](UpdatePartitionCountRequestData.md)|  | [optional]

### Return type

[**TopicData**](TopicData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The topic. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

