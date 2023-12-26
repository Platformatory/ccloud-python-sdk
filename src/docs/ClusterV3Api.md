# openapi_client.ClusterV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kafka_cluster**](ClusterV3Api.md#get_kafka_cluster) | **GET** /kafka/v3/clusters/{cluster_id} | Get Cluster


# **get_kafka_cluster**
> ClusterData get_kafka_cluster(cluster_id)

Get Cluster

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return the Kafka cluster with the specified ``cluster_id``.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import cluster__v3_api
from openapi_client.model.cluster_data import ClusterData
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
    api_instance = cluster__v3_api.ClusterV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Cluster
        api_response = api_instance.get_kafka_cluster(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterV3Api->get_kafka_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |

### Return type

[**ClusterData**](ClusterData.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Kafka cluster. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

