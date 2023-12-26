# openapi_client.ACLV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_kafka_acls**](ACLV3Api.md#batch_create_kafka_acls) | **POST** /kafka/v3/clusters/{cluster_id}/acls:batch | Batch Create ACLs
[**create_kafka_acls**](ACLV3Api.md#create_kafka_acls) | **POST** /kafka/v3/clusters/{cluster_id}/acls | Create an ACL
[**delete_kafka_acls**](ACLV3Api.md#delete_kafka_acls) | **DELETE** /kafka/v3/clusters/{cluster_id}/acls | Delete ACLs
[**get_kafka_acls**](ACLV3Api.md#get_kafka_acls) | **GET** /kafka/v3/clusters/{cluster_id}/acls | List ACLs


# **batch_create_kafka_acls**
> batch_create_kafka_acls(cluster_id)

Batch Create ACLs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create ACLs.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import acl__v3_api
from openapi_client.model.create_acl_request_data_list import CreateAclRequestDataList
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
    api_instance = acl__v3_api.ACLV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    create_acl_request_data_list = CreateAclRequestDataList(None) # CreateAclRequestDataList | The batch ACL creation request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Batch Create ACLs
        api_instance.batch_create_kafka_acls(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->batch_create_kafka_acls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Batch Create ACLs
        api_instance.batch_create_kafka_acls(cluster_id, create_acl_request_data_list=create_acl_request_data_list)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->batch_create_kafka_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **create_acl_request_data_list** | [**CreateAclRequestDataList**](CreateAclRequestDataList.md)| The batch ACL creation request. | [optional]

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
**201** | Created |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kafka_acls**
> create_kafka_acls(cluster_id)

Create an ACL

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create an ACL.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import acl__v3_api
from openapi_client.model.create_acl_request_data import CreateAclRequestData
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
    api_instance = acl__v3_api.ACLV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    create_acl_request_data = CreateAclRequestData(
        resource_type=AclResourceType("UNKNOWN"),
        resource_name="resource_name_example",
        pattern_type="pattern_type_example",
        principal="principal_example",
        host="host_example",
        operation="operation_example",
        permission="permission_example",
    ) # CreateAclRequestData | The ACL creation request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an ACL
        api_instance.create_kafka_acls(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->create_kafka_acls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an ACL
        api_instance.create_kafka_acls(cluster_id, create_acl_request_data=create_acl_request_data)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->create_kafka_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **create_acl_request_data** | [**CreateAclRequestData**](CreateAclRequestData.md)| The ACL creation request. | [optional]

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
**201** | Created |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_acls**
> InlineResponse2004 delete_kafka_acls(cluster_id, resource_type, pattern_type, operation, permission)

Delete ACLs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete the ACLs that match the search criteria.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import acl__v3_api
from openapi_client.model.inline_response2004 import InlineResponse2004
from openapi_client.model.acl_resource_type import AclResourceType
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
    api_instance = acl__v3_api.ACLV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    resource_type = AclResourceType("UNKNOWN") # AclResourceType | The ACL resource type.
    pattern_type = "pattern_type_example" # str | The ACL pattern type.
    operation = "operation_example" # str | The ACL operation.
    permission = "permission_example" # str | The ACL permission.
    resource_name = "resource_name_example" # str | The ACL resource name. (optional)
    principal = "principal_example" # str | The ACL principal. This is the Service Account name or user name. (optional)
    host = "host_example" # str | The ACL host. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete ACLs
        api_response = api_instance.delete_kafka_acls(cluster_id, resource_type, pattern_type, operation, permission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->delete_kafka_acls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete ACLs
        api_response = api_instance.delete_kafka_acls(cluster_id, resource_type, pattern_type, operation, permission, resource_name=resource_name, principal=principal, host=host)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->delete_kafka_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **resource_type** | **AclResourceType**| The ACL resource type. |
 **pattern_type** | **str**| The ACL pattern type. |
 **operation** | **str**| The ACL operation. |
 **permission** | **str**| The ACL permission. |
 **resource_name** | **str**| The ACL resource name. | [optional]
 **principal** | **str**| The ACL principal. This is the Service Account name or user name. | [optional]
 **host** | **str**| The ACL host. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of deleted ACLs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_acls**
> AclDataList get_kafka_acls(cluster_id)

List ACLs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Return a list of ACLs that match the search criteria.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):

```python
import time
import openapi_client
from openapi_client.api import acl__v3_api
from openapi_client.model.acl_data_list import AclDataList
from openapi_client.model.acl_resource_type import AclResourceType
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
    api_instance = acl__v3_api.ACLV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
    resource_type = AclResourceType("UNKNOWN") # AclResourceType | The ACL resource type. (optional)
    resource_name = "resource_name_example" # str | The ACL resource name. (optional)
    pattern_type = "pattern_type_example" # str | The ACL pattern type. (optional)
    principal = "principal_example" # str | The ACL principal. This is the Service Account name or user name. (optional)
    host = "host_example" # str | The ACL host. (optional)
    operation = "operation_example" # str | The ACL operation. (optional)
    permission = "permission_example" # str | The ACL permission. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ACLs
        api_response = api_instance.get_kafka_acls(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->get_kafka_acls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ACLs
        api_response = api_instance.get_kafka_acls(cluster_id, resource_type=resource_type, resource_name=resource_name, pattern_type=pattern_type, principal=principal, host=host, operation=operation, permission=permission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->get_kafka_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. |
 **resource_type** | **AclResourceType**| The ACL resource type. | [optional]
 **resource_name** | **str**| The ACL resource name. | [optional]
 **pattern_type** | **str**| The ACL pattern type. | [optional]
 **principal** | **str**| The ACL principal. This is the Service Account name or user name. | [optional]
 **host** | **str**| The ACL host. | [optional]
 **operation** | **str**| The ACL operation. | [optional]
 **permission** | **str**| The ACL permission. | [optional]

### Return type

[**AclDataList**](AclDataList.md)

### Authorization

[external-access-token](../README.md#external-access-token), [resource-api-key](../README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of ACLs. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

