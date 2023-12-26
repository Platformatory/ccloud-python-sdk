# openapi_client.SearchV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_using_attribute**](SearchV1Api.md#search_using_attribute) | **GET** /catalog/v1/search/attribute | Search by Attribute
[**search_using_basic**](SearchV1Api.md#search_using_basic) | **GET** /catalog/v1/search/basic | Search by Fulltext Query


# **search_using_attribute**
> SearchResult search_using_attribute()

Search by Attribute

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve data for the specified attribute search query.

### Example


```python
import time
import openapi_client
from openapi_client.api import search__v1_api
from openapi_client.model.search_result import SearchResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search__v1_api.SearchV1Api(api_client)
    type = [
        "type_example",
    ] # [str] | Limit the result to only entities of specified types (optional)
    attr = [
        "attr_example",
    ] # [str] | One of more additional attributes to return in the response (optional)
    attr_name = [
        "attrName_example",
    ] # [str] | The attribute to search (optional)
    attr_value_prefix = [
        "attrValuePrefix_example",
    ] # [str] | The prefix for the attribute value to search (optional)
    tag = "tag_example" # str | Limit the result to only entities tagged with the given tag (optional)
    sort_by = "sortBy_example" # str | An attribute to sort by (optional)
    sort_order = "ASCENDING" # str | Sort order, either ASCENDING (default) or DESCENDING (optional)
    deleted = True # bool | Whether to include deleted entities (optional)
    limit = 1 # int | Limit the result set to only include the specified number of entries (optional)
    offset = 1 # int | Start offset of the result set (useful for pagination) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search by Attribute
        api_response = api_instance.search_using_attribute(type=type, attr=attr, attr_name=attr_name, attr_value_prefix=attr_value_prefix, tag=tag, sort_by=sort_by, sort_order=sort_order, deleted=deleted, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchV1Api->search_using_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **[str]**| Limit the result to only entities of specified types | [optional]
 **attr** | **[str]**| One of more additional attributes to return in the response | [optional]
 **attr_name** | **[str]**| The attribute to search | [optional]
 **attr_value_prefix** | **[str]**| The prefix for the attribute value to search | [optional]
 **tag** | **str**| Limit the result to only entities tagged with the given tag | [optional]
 **sort_by** | **str**| An attribute to sort by | [optional]
 **sort_order** | **str**| Sort order, either ASCENDING (default) or DESCENDING | [optional]
 **deleted** | **bool**| Whether to include deleted entities | [optional]
 **limit** | **int**| Limit the result set to only include the specified number of entries | [optional]
 **offset** | **int**| Start offset of the result set (useful for pagination) | [optional]

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On successful search query with some results, might return an empty list if execution succeeded without any results |  -  |
**400** | Invalid wildcard or query parameters |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_basic**
> SearchResult search_using_basic()

Search by Fulltext Query

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve data for the specified fulltext query.

### Example


```python
import time
import openapi_client
from openapi_client.api import search__v1_api
from openapi_client.model.search_result import SearchResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search__v1_api.SearchV1Api(api_client)
    query = "query_example" # str | The full-text query (optional)
    type = [
        "type_example",
    ] # [str] | Limit the result to only entities of specified types (optional)
    attr = [
        "attr_example",
    ] # [str] | One of more additional attributes to return in the response (optional)
    tag = "tag_example" # str | Limit the result to only entities tagged with the given tag (optional)
    sort_by = "sortBy_example" # str | An attribute to sort by (optional)
    sort_order = "ASCENDING" # str | Sort order, either ASCENDING (default) or DESCENDING (optional)
    deleted = True # bool | Whether to include deleted entities (optional)
    limit = 1 # int | Limit the result set to only include the specified number of entries (optional)
    offset = 1 # int | Start offset of the result set (useful for pagination) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search by Fulltext Query
        api_response = api_instance.search_using_basic(query=query, type=type, attr=attr, tag=tag, sort_by=sort_by, sort_order=sort_order, deleted=deleted, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchV1Api->search_using_basic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The full-text query | [optional]
 **type** | **[str]**| Limit the result to only entities of specified types | [optional]
 **attr** | **[str]**| One of more additional attributes to return in the response | [optional]
 **tag** | **str**| Limit the result to only entities tagged with the given tag | [optional]
 **sort_by** | **str**| An attribute to sort by | [optional]
 **sort_order** | **str**| Sort order, either ASCENDING (default) or DESCENDING | [optional]
 **deleted** | **bool**| Whether to include deleted entities | [optional]
 **limit** | **int**| Limit the result set to only include the specified number of entries | [optional]
 **offset** | **int**| Start offset of the result set (useful for pagination) | [optional]

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On successful fulltext query with some results, might return an empty list if execution succeeded without any results |  -  |
**400** | Invalid fulltext or query parameters |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

