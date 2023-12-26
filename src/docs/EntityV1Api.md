# openapi_client.EntityV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_metadata**](EntityV1Api.md#create_business_metadata) | **POST** /catalog/v1/entity/businessmetadata | Bulk Create Business Metadata
[**create_tags**](EntityV1Api.md#create_tags) | **POST** /catalog/v1/entity/tags | Bulk Create Tags
[**delete_business_metadata**](EntityV1Api.md#delete_business_metadata) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata/{bmName} | Delete a Business Metadata for an Entity
[**delete_tag**](EntityV1Api.md#delete_tag) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags/{tagName} | Delete a Tag for an Entity
[**get_business_metadata**](EntityV1Api.md#get_business_metadata) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata | Read Business Metadata for an Entity
[**get_by_unique_attributes**](EntityV1Api.md#get_by_unique_attributes) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName} | Read an Entity
[**get_tags**](EntityV1Api.md#get_tags) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags | Read Tags for an Entity
[**partial_entity_update**](EntityV1Api.md#partial_entity_update) | **PUT** /catalog/v1/entity | Update an Entity Attribute
[**update_business_metadata**](EntityV1Api.md#update_business_metadata) | **PUT** /catalog/v1/entity/businessmetadata | Bulk Update Business Metadata
[**update_tags**](EntityV1Api.md#update_tags) | **PUT** /catalog/v1/entity/tags | Bulk Update Tags


# **create_business_metadata**
> [BusinessMetadataResponse] create_business_metadata()

Bulk Create Business Metadata

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to create multiple business metadata.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.business_metadata import BusinessMetadata
from openapi_client.model.business_metadata_response import BusinessMetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    business_metadata = [
        BusinessMetadata(
            type_name="type_name_example",
            attributes={},
            entity_type="entity_type_example",
            entity_name="entity_name_example",
        ),
    ] # [BusinessMetadata] | The business metadata (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Create Business Metadata
        api_response = api_instance.create_business_metadata(business_metadata=business_metadata)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->create_business_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata** | [**[BusinessMetadata]**](BusinessMetadata.md)| The business metadata | [optional]

### Return type

[**[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata. Errored business metadata will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tags**
> [TagResponse] create_tags()

Bulk Create Tags

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to create multiple tags.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.tag import Tag
from openapi_client.model.tag_response import TagResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    tag = [
        Tag(
            type_name="type_name_example",
            attributes={},
            entity_guid="entity_guid_example",
            entity_status="ACTIVE",
            propagate=True,
            validity_periods=[
                TimeBoundary(
                    start_time="start_time_example",
                    end_time="end_time_example",
                    time_zone="time_zone_example",
                ),
            ],
            remove_propagations_on_entity_delete=True,
            entity_type="entity_type_example",
            entity_name="entity_name_example",
        ),
    ] # [Tag] | The tags (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Create Tags
        api_response = api_instance.create_tags(tag=tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->create_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**[Tag]**](Tag.md)| The tags | [optional]

### Return type

[**[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags. Errored tags will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_metadata**
> delete_business_metadata(type_name, qualified_name, bm_name)

Delete a Business Metadata for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a business metadata on an entity.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    type_name = "typeName_example" # str | The type of the entity
    qualified_name = "qualifiedName_example" # str | The qualified name of the entity
    bm_name = "bmName_example" # str | The name of the business metadata

    # example passing only required values which don't have defaults set
    try:
        # Delete a Business Metadata for an Entity
        api_instance.delete_business_metadata(type_name, qualified_name, bm_name)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->delete_business_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity |
 **qualified_name** | **str**| The qualified name of the entity |
 **bm_name** | **str**| The name of the business metadata |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(type_name, qualified_name, tag_name)

Delete a Tag for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a tag for an entity.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    type_name = "typeName_example" # str | The type of the entity
    qualified_name = "qualifiedName_example" # str | The qualified name of the entity
    tag_name = "tagName_example" # str | The name of the tag

    # example passing only required values which don't have defaults set
    try:
        # Delete a Tag for an Entity
        api_instance.delete_tag(type_name, qualified_name, tag_name)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity |
 **qualified_name** | **str**| The qualified name of the entity |
 **tag_name** | **str**| The name of the tag |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_metadata**
> [BusinessMetadataResponse] get_business_metadata(type_name, qualified_name)

Read Business Metadata for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Gets the list of business metadata for a given entity represented by a qualified name.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.business_metadata_response import BusinessMetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    type_name = "typeName_example" # str | The type of the entity
    qualified_name = "qualifiedName_example" # str | The qualified name of the entity

    # example passing only required values which don't have defaults set
    try:
        # Read Business Metadata for an Entity
        api_response = api_instance.get_business_metadata(type_name, qualified_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->get_business_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity |
 **qualified_name** | **str**| The qualified name of the entity |

### Return type

[**[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_unique_attributes**
> EntityWithExtInfo get_by_unique_attributes(type_name, qualified_name)

Read an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Fetch complete definition of an entity given its type and unique attribute.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.entity_with_ext_info import EntityWithExtInfo
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    type_name = "typeName_example" # str | The type of the entity
    qualified_name = "qualifiedName_example" # str | The qualified name of the entity
    min_ext_info = False # bool | Whether to populate on header and schema attributes (optional) if omitted the server will use the default value of False
    ignore_relationships = False # bool | Whether to ignore relationships (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Read an Entity
        api_response = api_instance.get_by_unique_attributes(type_name, qualified_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->get_by_unique_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read an Entity
        api_response = api_instance.get_by_unique_attributes(type_name, qualified_name, min_ext_info=min_ext_info, ignore_relationships=ignore_relationships)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->get_by_unique_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity |
 **qualified_name** | **str**| The qualified name of the entity |
 **min_ext_info** | **bool**| Whether to populate on header and schema attributes | [optional] if omitted the server will use the default value of False
 **ignore_relationships** | **bool**| Whether to ignore relationships | [optional] if omitted the server will use the default value of False

### Return type

[**EntityWithExtInfo**](EntityWithExtInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The entity |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> [TagResponse] get_tags(type_name, qualified_name)

Read Tags for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Gets the list of tags for a given entity represented by a qualified name.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.tag_response import TagResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    type_name = "typeName_example" # str | The type of the entity
    qualified_name = "qualifiedName_example" # str | The qualified name of the entity

    # example passing only required values which don't have defaults set
    try:
        # Read Tags for an Entity
        api_response = api_instance.get_tags(type_name, qualified_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->get_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity |
 **qualified_name** | **str**| The qualified name of the entity |

### Return type

[**[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_entity_update**
> EntityPartialUpdateResponse partial_entity_update()

Update an Entity Attribute

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Partially update an entity attribute.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.entity_with_ext_info import EntityWithExtInfo
from openapi_client.model.entity_partial_update_response import EntityPartialUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    entity_with_ext_info = EntityWithExtInfo(
        referred_entities={
            "key": Entity(
                type_name="type_name_example",
                attributes={},
                guid="guid_example",
                home_id="home_id_example",
                is_proxy=True,
                is_incomplete=True,
                provenance_type=1,
                status="ACTIVE",
                created_by="created_by_example",
                updated_by="updated_by_example",
                create_time=1,
                update_time=1,
                version=1,
                relationship_attributes={},
                classifications=[
                    Classification(
                        type_name="type_name_example",
                        attributes={
                            "key": {},
                        },
                        entity_guid="entity_guid_example",
                        entity_status="ACTIVE",
                        propagate=True,
                        validity_periods=[
                            TimeBoundary(
                                start_time="start_time_example",
                                end_time="end_time_example",
                                time_zone="time_zone_example",
                            ),
                        ],
                        remove_propagations_on_entity_delete=True,
                    ),
                ],
                meanings=[
                    TermAssignmentHeader(
                        term_guid="term_guid_example",
                        relation_guid="relation_guid_example",
                        description="description_example",
                        display_text="display_text_example",
                        expression="expression_example",
                        created_by="created_by_example",
                        steward="steward_example",
                        source="source_example",
                        confidence=1,
                        status="DISCOVERED",
                    ),
                ],
                custom_attributes={
                    "key": "key_example",
                },
                business_attributes={
                    "key": {},
                },
                labels=[
                    "labels_example",
                ],
                proxy=True,
            ),
        },
        entity=Entity(
            type_name="type_name_example",
            attributes={},
            guid="guid_example",
            home_id="home_id_example",
            is_proxy=True,
            is_incomplete=True,
            provenance_type=1,
            status="ACTIVE",
            created_by="created_by_example",
            updated_by="updated_by_example",
            create_time=1,
            update_time=1,
            version=1,
            relationship_attributes={},
            classifications=[
                Classification(
                    type_name="type_name_example",
                    attributes={
                        "key": {},
                    },
                    entity_guid="entity_guid_example",
                    entity_status="ACTIVE",
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="start_time_example",
                            end_time="end_time_example",
                            time_zone="time_zone_example",
                        ),
                    ],
                    remove_propagations_on_entity_delete=True,
                ),
            ],
            meanings=[
                TermAssignmentHeader(
                    term_guid="term_guid_example",
                    relation_guid="relation_guid_example",
                    description="description_example",
                    display_text="display_text_example",
                    expression="expression_example",
                    created_by="created_by_example",
                    steward="steward_example",
                    source="source_example",
                    confidence=1,
                    status="DISCOVERED",
                ),
            ],
            custom_attributes={
                "key": "key_example",
            },
            business_attributes={
                "key": {},
            },
            labels=[
                "labels_example",
            ],
            proxy=True,
        ),
    ) # EntityWithExtInfo | The entity to update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Entity Attribute
        api_response = api_instance.partial_entity_update(entity_with_ext_info=entity_with_ext_info)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->partial_entity_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_with_ext_info** | [**EntityWithExtInfo**](EntityWithExtInfo.md)| The entity to update | [optional]

### Return type

[**EntityPartialUpdateResponse**](EntityPartialUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated entity |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_metadata**
> [BusinessMetadataResponse] update_business_metadata()

Bulk Update Business Metadata

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to update multiple business metadata.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.business_metadata import BusinessMetadata
from openapi_client.model.business_metadata_response import BusinessMetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    business_metadata = [
        BusinessMetadata(
            type_name="type_name_example",
            attributes={},
            entity_type="entity_type_example",
            entity_name="entity_name_example",
        ),
    ] # [BusinessMetadata] | The business metadata (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Update Business Metadata
        api_response = api_instance.update_business_metadata(business_metadata=business_metadata)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->update_business_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata** | [**[BusinessMetadata]**](BusinessMetadata.md)| The business metadata | [optional]

### Return type

[**[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata. Errored business metadata will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tags**
> [TagResponse] update_tags()

Bulk Update Tags

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to update multiple tags.

### Example


```python
import time
import openapi_client
from openapi_client.api import entity__v1_api
from openapi_client.model.tag import Tag
from openapi_client.model.tag_response import TagResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity__v1_api.EntityV1Api(api_client)
    tag = [
        Tag(
            type_name="type_name_example",
            attributes={},
            entity_guid="entity_guid_example",
            entity_status="ACTIVE",
            propagate=True,
            validity_periods=[
                TimeBoundary(
                    start_time="start_time_example",
                    end_time="end_time_example",
                    time_zone="time_zone_example",
                ),
            ],
            remove_propagations_on_entity_delete=True,
            entity_type="entity_type_example",
            entity_name="entity_name_example",
        ),
    ] # [Tag] | The tags (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Update Tags
        api_response = api_instance.update_tags(tag=tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntityV1Api->update_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**[Tag]**](Tag.md)| The tags | [optional]

### Return type

[**[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags. Errored tags will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

