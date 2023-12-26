# openapi_client.ClusterLinkingV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kafka_link**](ClusterLinkingV3Api.md#create_kafka_link) | **POST** /kafka/v3/clusters/{cluster_id}/links | Create a cluster link
[**create_kafka_mirror_topic**](ClusterLinkingV3Api.md#create_kafka_mirror_topic) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | Create a mirror topic
[**delete_kafka_link**](ClusterLinkingV3Api.md#delete_kafka_link) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Delete the cluster link
[**delete_kafka_link_config**](ClusterLinkingV3Api.md#delete_kafka_link_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Reset the given config to default value
[**get_kafka_link**](ClusterLinkingV3Api.md#get_kafka_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Describe the cluster link
[**get_kafka_link_configs**](ClusterLinkingV3Api.md#get_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Describe the config under the cluster link
[**list_kafka_link_configs**](ClusterLinkingV3Api.md#list_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs | List all configs of the cluster link
[**list_kafka_links**](ClusterLinkingV3Api.md#list_kafka_links) | **GET** /kafka/v3/clusters/{cluster_id}/links | List all cluster links in the dest cluster
[**list_kafka_mirror_topics**](ClusterLinkingV3Api.md#list_kafka_mirror_topics) | **GET** /kafka/v3/clusters/{cluster_id}/links/-/mirrors | List mirror topics
[**list_kafka_mirror_topics_under_link**](ClusterLinkingV3Api.md#list_kafka_mirror_topics_under_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | List mirror topics
[**read_kafka_mirror_topic**](ClusterLinkingV3Api.md#read_kafka_mirror_topic) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors/{mirror_topic_name} | Describe the mirror topic
[**update_kafka_link_config**](ClusterLinkingV3Api.md#update_kafka_link_config) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Alter the config under the cluster link
[**update_kafka_link_config_batch**](ClusterLinkingV3Api.md#update_kafka_link_config_batch) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs:alter | Batch Alter Cluster Link Configs
[**update_kafka_mirror_topics_failover**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_failover) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:failover | Failover the mirror topics
[**update_kafka_mirror_topics_pause**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_pause) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:pause | Pause the mirror topics
[**update_kafka_mirror_topics_promote**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_promote) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:promote | Promote the mirror topics
[**update_kafka_mirror_topics_resume**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_resume) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:resume | Resume the mirror topics


# **create_kafka_link**
> create_kafka_link(cluster_id, link_name)

Create a cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.error import Error
from openapi_client.model.create_link_request_data import CreateLinkRequestData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    validate_link = False # bool | To synchronously validate that the source cluster ID is expected and the dest cluster has the permission to read topics in the source cluster. Default: true (optional)
    create_link_request_data = CreateLinkRequestData(
        source_cluster_id="source_cluster_id_example",
        destination_cluster_id="destination_cluster_id_example",
        remote_cluster_id="remote_cluster_id_example",
        cluster_link_id="cluster_link_id_example",
        configs=[
            ConfigData(None),
        ],
    ) # CreateLinkRequestData | Create a cluster link (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a cluster link
        api_instance.create_kafka_link(cluster_id, link_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_link: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a cluster link
        api_instance.create_kafka_link(cluster_id, link_name, validate_only=validate_only, validate_link=validate_link, create_link_request_data=create_link_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **validate_link** | **bool**| To synchronously validate that the source cluster ID is expected and the dest cluster has the permission to read topics in the source cluster. Default: true | [optional]
 **create_link_request_data** | [**CreateLinkRequestData**](CreateLinkRequestData.md)| Create a cluster link | [optional]

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
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kafka_mirror_topic**
> create_kafka_mirror_topic(cluster_id, link_name)

Create a mirror topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create a topic in the destination cluster mirroring a topic in the source cluster

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.create_mirror_topic_request_data import CreateMirrorTopicRequestData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    create_mirror_topic_request_data = CreateMirrorTopicRequestData(
        source_topic_name="source_topic_name_example",
        mirror_topic_name="mirror_topic_name_example",
        replication_factor=1,
        configs=[
            ConfigData(None),
        ],
    ) # CreateMirrorTopicRequestData | Name and configs of the topics mirroring from and mirroring to. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a mirror topic
        api_instance.create_kafka_mirror_topic(cluster_id, link_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_mirror_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a mirror topic
        api_instance.create_kafka_mirror_topic(cluster_id, link_name, create_mirror_topic_request_data=create_mirror_topic_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_mirror_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **create_mirror_topic_request_data** | [**CreateMirrorTopicRequestData**](CreateMirrorTopicRequestData.md)| Name and configs of the topics mirroring from and mirroring to. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). | [optional]

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
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_link**
> delete_kafka_link(cluster_id, link_name)

Delete the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    force = False # bool | Force the action. Default: false (optional)
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the cluster link
        api_instance.delete_kafka_link(cluster_id, link_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->delete_kafka_link: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the cluster link
        api_instance.delete_kafka_link(cluster_id, link_name, force=force, validate_only=validate_only)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->delete_kafka_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **force** | **bool**| Force the action. Default: false | [optional]
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]

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
**200** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_link_config**
> delete_kafka_link_config(cluster_id, link_name, config_name)

Reset the given config to default value

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    config_name = "consumer.offset.sync.enable" # str | The link config name

    # example passing only required values which don't have defaults set
    try:
        # Reset the given config to default value
        api_instance.delete_kafka_link_config(cluster_id, link_name, config_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->delete_kafka_link_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **config_name** | **str**| The link config name |

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
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_link**
> ListLinksResponseData get_kafka_link(cluster_id, link_name)

Describe the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.list_links_response_data import ListLinksResponseData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name

    # example passing only required values which don't have defaults set
    try:
        # Describe the cluster link
        api_response = api_instance.get_kafka_link(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->get_kafka_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |

### Return type

[**ListLinksResponseData**](ListLinksResponseData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single link name and properties |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_link_configs**
> ListLinkConfigsResponseData get_kafka_link_configs(cluster_id, link_name, config_name)

Describe the config under the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.error import Error
from openapi_client.model.list_link_configs_response_data import ListLinkConfigsResponseData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    config_name = "consumer.offset.sync.enable" # str | The link config name

    # example passing only required values which don't have defaults set
    try:
        # Describe the config under the cluster link
        api_response = api_instance.get_kafka_link_configs(cluster_id, link_name, config_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->get_kafka_link_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **config_name** | **str**| The link config name |

### Return type

[**ListLinkConfigsResponseData**](ListLinkConfigsResponseData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config name and value |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_link_configs**
> ListLinkConfigsResponseDataList list_kafka_link_configs(cluster_id, link_name)

List all configs of the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.error import Error
from openapi_client.model.list_link_configs_response_data_list import ListLinkConfigsResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name

    # example passing only required values which don't have defaults set
    try:
        # List all configs of the cluster link
        api_response = api_instance.list_kafka_link_configs(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_link_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |

### Return type

[**ListLinkConfigsResponseDataList**](ListLinkConfigsResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config name and value |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_links**
> ListLinksResponseDataList list_kafka_links(cluster_id)

List all cluster links in the dest cluster

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.error import Error
from openapi_client.model.list_links_response_data_list import ListLinksResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # List all cluster links in the dest cluster
        api_response = api_instance.list_kafka_links(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**ListLinksResponseDataList**](ListLinksResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of link names and properties |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_mirror_topics**
> ListMirrorTopicsResponseDataList list_kafka_mirror_topics(cluster_id)

List mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  List all mirror topics in the cluster

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.list_mirror_topics_response_data_list import ListMirrorTopicsResponseDataList
from openapi_client.model.error import Error
from openapi_client.model.mirror_topic_status import MirrorTopicStatus
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    mirror_status = MirrorTopicStatus("ACTIVE") # MirrorTopicStatus | The status of the mirror topic. If not specified, all mirror topics will be returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics(cluster_id, mirror_status=mirror_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **mirror_status** | **MirrorTopicStatus**| The status of the mirror topic. If not specified, all mirror topics will be returned. | [optional]

### Return type

[**ListMirrorTopicsResponseDataList**](ListMirrorTopicsResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of mirror topics |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kafka_mirror_topics_under_link**
> ListMirrorTopicsResponseDataList list_kafka_mirror_topics_under_link(cluster_id, link_name)

List mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  List all mirror topics under the link

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.list_mirror_topics_response_data_list import ListMirrorTopicsResponseDataList
from openapi_client.model.error import Error
from openapi_client.model.mirror_topic_status import MirrorTopicStatus
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    mirror_status = MirrorTopicStatus("ACTIVE") # MirrorTopicStatus | The status of the mirror topic. If not specified, all mirror topics will be returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics_under_link(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics_under_link: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics_under_link(cluster_id, link_name, mirror_status=mirror_status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics_under_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **mirror_status** | **MirrorTopicStatus**| The status of the mirror topic. If not specified, all mirror topics will be returned. | [optional]

### Return type

[**ListMirrorTopicsResponseDataList**](ListMirrorTopicsResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of mirror topics |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_kafka_mirror_topic**
> ListMirrorTopicsResponseData read_kafka_mirror_topic(cluster_id, link_name, mirror_topic_name)

Describe the mirror topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.list_mirror_topics_response_data import ListMirrorTopicsResponseData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    mirror_topic_name = "topic-1" # str | Cluster Linking mirror topic name

    # example passing only required values which don't have defaults set
    try:
        # Describe the mirror topic
        api_response = api_instance.read_kafka_mirror_topic(cluster_id, link_name, mirror_topic_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->read_kafka_mirror_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **mirror_topic_name** | **str**| Cluster Linking mirror topic name |

### Return type

[**ListMirrorTopicsResponseData**](ListMirrorTopicsResponseData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of the mirror topic |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_link_config**
> update_kafka_link_config(cluster_id, link_name, config_name)

Alter the config under the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.update_link_config_request_data import UpdateLinkConfigRequestData
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    config_name = "consumer.offset.sync.enable" # str | The link config name
    update_link_config_request_data = UpdateLinkConfigRequestData(
        value="value_example",
    ) # UpdateLinkConfigRequestData | Link config value to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Alter the config under the cluster link
        api_instance.update_kafka_link_config(cluster_id, link_name, config_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Alter the config under the cluster link
        api_instance.update_kafka_link_config(cluster_id, link_name, config_name, update_link_config_request_data=update_link_config_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **config_name** | **str**| The link config name |
 **update_link_config_request_data** | [**UpdateLinkConfigRequestData**](UpdateLinkConfigRequestData.md)| Link config value to update | [optional]

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
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_link_config_batch**
> update_kafka_link_config_batch(cluster_id, link_name)

Batch Alter Cluster Link Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Batch Alter Cluster Link Configs

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_config_batch_request_data = AlterConfigBatchRequestData(
        data=[
            AlterConfigBatchRequestDataData(
                name="name_example",
                value="value_example",
                operation="operation_example",
            ),
        ],
        validate_only=True,
    ) # AlterConfigBatchRequestData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Batch Alter Cluster Link Configs
        api_instance.update_kafka_link_config_batch(cluster_id, link_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Batch Alter Cluster Link Configs
        api_instance.update_kafka_link_config_batch(cluster_id, link_name, validate_only=validate_only, alter_config_batch_request_data=alter_config_batch_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **alter_config_batch_request_data** | [**AlterConfigBatchRequestData**](AlterConfigBatchRequestData.md)|  | [optional]

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
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_mirror_topics_failover**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_failover(cluster_id, link_name)

Failover the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.alter_mirrors_request_data import AlterMirrorsRequestData
from openapi_client.model.error import Error
from openapi_client.model.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = AlterMirrorsRequestData(
        mirror_topic_names=[
            "mirror_topic_names_example",
        ],
        mirror_topic_name_pattern="mirror_topic_name_pattern_example",
    ) # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Failover the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_failover(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_failover: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Failover the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_failover(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_failover: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional]

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_mirror_topics_pause**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_pause(cluster_id, link_name)

Pause the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.alter_mirrors_request_data import AlterMirrorsRequestData
from openapi_client.model.error import Error
from openapi_client.model.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = AlterMirrorsRequestData(
        mirror_topic_names=[
            "mirror_topic_names_example",
        ],
        mirror_topic_name_pattern="mirror_topic_name_pattern_example",
    ) # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Pause the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_pause(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_pause: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pause the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_pause(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_pause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional]

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_mirror_topics_promote**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_promote(cluster_id, link_name)

Promote the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.alter_mirrors_request_data import AlterMirrorsRequestData
from openapi_client.model.error import Error
from openapi_client.model.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = AlterMirrorsRequestData(
        mirror_topic_names=[
            "mirror_topic_names_example",
        ],
        mirror_topic_name_pattern="mirror_topic_name_pattern_example",
    ) # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Promote the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_promote(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_promote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Promote the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_promote(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_promote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional]

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kafka_mirror_topics_resume**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_resume(cluster_id, link_name)

Resume the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster_linking__v3_api
from openapi_client.model.alter_mirrors_request_data import AlterMirrorsRequestData
from openapi_client.model.error import Error
from openapi_client.model.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
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
    api_instance = cluster_linking__v3_api.ClusterLinkingV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    link_name = "link-sb1" # str | The link name
    validate_only = False # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = AlterMirrorsRequestData(
        mirror_topic_names=[
            "mirror_topic_names_example",
        ],
        mirror_topic_name_pattern="mirror_topic_name_pattern_example",
    ) # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resume the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_resume(cluster_id, link_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_resume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resume the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_resume(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_resume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **link_name** | **str**| The link name |
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional]
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional]

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

