# openapi_client.TypesV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_metadata_defs**](TypesV1Api.md#create_business_metadata_defs) | **POST** /catalog/v1/types/businessmetadatadefs | Bulk Create Business Metadata Definitions
[**create_tag_defs**](TypesV1Api.md#create_tag_defs) | **POST** /catalog/v1/types/tagdefs | Bulk Create Tag Definitions
[**delete_business_metadata_def**](TypesV1Api.md#delete_business_metadata_def) | **DELETE** /catalog/v1/types/businessmetadatadefs/{bmName} | Delete Business Metadata Definition
[**delete_tag_def**](TypesV1Api.md#delete_tag_def) | **DELETE** /catalog/v1/types/tagdefs/{tagName} | Delete Tag Definition
[**get_all_business_metadata_defs**](TypesV1Api.md#get_all_business_metadata_defs) | **GET** /catalog/v1/types/businessmetadatadefs | Bulk Read Business Metadata Definitions
[**get_all_tag_defs**](TypesV1Api.md#get_all_tag_defs) | **GET** /catalog/v1/types/tagdefs | Bulk Read Tag Definitions
[**get_business_metadata_def_by_name**](TypesV1Api.md#get_business_metadata_def_by_name) | **GET** /catalog/v1/types/businessmetadatadefs/{bmName} | Read Business Metadata Definition
[**get_tag_def_by_name**](TypesV1Api.md#get_tag_def_by_name) | **GET** /catalog/v1/types/tagdefs/{tagName} | Read Tag Definition
[**update_business_metadata_defs**](TypesV1Api.md#update_business_metadata_defs) | **PUT** /catalog/v1/types/businessmetadatadefs | Bulk Update Business Metadata Definitions
[**update_tag_defs**](TypesV1Api.md#update_tag_defs) | **PUT** /catalog/v1/types/tagdefs | Bulk Update Tag Definitions


# **create_business_metadata_defs**
> [BusinessMetadataDefResponse] create_business_metadata_defs()

Bulk Create Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk create API for business metadata definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.business_metadata_def_response import BusinessMetadataDefResponse
from openapi_client.model.business_metadata_def import BusinessMetadataDef
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    business_metadata_def = [
        BusinessMetadataDef(
            category="PRIMITIVE",
            guid="guid_example",
            created_by="created_by_example",
            updated_by="updated_by_example",
            create_time=1,
            update_time=1,
            version=1,
            name="name_example",
            description="description_example",
            type_version="type_version_example",
            service_type="service_type_example",
            options={
                "key": "key_example",
            },
            attribute_defs=[
                AttributeDef(
                    name="name_example",
                    type_name="type_name_example",
                    is_optional=True,
                    cardinality="SINGLE",
                    values_min_count=1,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="default_value_example",
                    description="description_example",
                    search_weight=1,
                    index_type="DEFAULT",
                    constraints=[
                        ConstraintDef(
                            type="type_example",
                            params={
                                "key": {},
                            },
                        ),
                    ],
                    options={
                        "key": "key_example",
                    },
                    display_name="display_name_example",
                ),
            ],
        ),
    ] # [BusinessMetadataDef] | The business metadata definitions to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Create Business Metadata Definitions
        api_response = api_instance.create_business_metadata_defs(business_metadata_def=business_metadata_def)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->create_business_metadata_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata_def** | [**[BusinessMetadataDef]**](BusinessMetadataDef.md)| The business metadata definitions to create | [optional]

### Return type

[**[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions. Errored business metadata definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag_defs**
> [TagDefResponse] create_tag_defs()

Bulk Create Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk create API for tag definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.tag_def import TagDef
from openapi_client.model.tag_def_response import TagDefResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    tag_def = [
        TagDef(
            category="PRIMITIVE",
            guid="guid_example",
            created_by="created_by_example",
            updated_by="updated_by_example",
            create_time=1,
            update_time=1,
            version=1,
            name="name_example",
            description="description_example",
            type_version="type_version_example",
            service_type="service_type_example",
            options={
                "key": "key_example",
            },
            attribute_defs=[
                AttributeDef(
                    name="name_example",
                    type_name="type_name_example",
                    is_optional=True,
                    cardinality="SINGLE",
                    values_min_count=1,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="default_value_example",
                    description="description_example",
                    search_weight=1,
                    index_type="DEFAULT",
                    constraints=[
                        ConstraintDef(
                            type="type_example",
                            params={
                                "key": {},
                            },
                        ),
                    ],
                    options={
                        "key": "key_example",
                    },
                    display_name="display_name_example",
                ),
            ],
            super_types=[
                "super_types_example",
            ],
            entity_types=[
                "entity_types_example",
            ],
            sub_types=[
                "sub_types_example",
            ],
        ),
    ] # [TagDef] | The tag definitions to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Create Tag Definitions
        api_response = api_instance.create_tag_defs(tag_def=tag_def)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->create_tag_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_def** | [**[TagDef]**](TagDef.md)| The tag definitions to create | [optional]

### Return type

[**[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions. Errored tag definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_metadata_def**
> delete_business_metadata_def(bm_name)

Delete Business Metadata Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete API for business metadata definition identified by its name.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    bm_name = "bmName_example" # str | The name of the business metadata definition

    # example passing only required values which don't have defaults set
    try:
        # Delete Business Metadata Definition
        api_instance.delete_business_metadata_def(bm_name)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->delete_business_metadata_def: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_name** | **str**| The name of the business metadata definition |

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

# **delete_tag_def**
> delete_tag_def(tag_name)

Delete Tag Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete API for tag definition identified by its name.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    tag_name = "tagName_example" # str | The name of the tag definition

    # example passing only required values which don't have defaults set
    try:
        # Delete Tag Definition
        api_instance.delete_tag_def(tag_name)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->delete_tag_def: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag definition |

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

# **get_all_business_metadata_defs**
> [BusinessMetadataDefResponse] get_all_business_metadata_defs()

Bulk Read Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk retrieval API for retrieving business metadata definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.business_metadata_def_response import BusinessMetadataDefResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    prefix = "prefix_example" # str | The prefix of a business metadata definition name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Read Business Metadata Definitions
        api_response = api_instance.get_all_business_metadata_defs(prefix=prefix)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->get_all_business_metadata_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The prefix of a business metadata definition name | [optional]

### Return type

[**[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tag_defs**
> [TagDefResponse] get_all_tag_defs()

Bulk Read Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk retrieval API for retrieving tag definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.tag_def_response import TagDefResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    prefix = "prefix_example" # str | The prefix of a tag definition name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Read Tag Definitions
        api_response = api_instance.get_all_tag_defs(prefix=prefix)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->get_all_tag_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The prefix of a tag definition name | [optional]

### Return type

[**[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_metadata_def_by_name**
> BusinessMetadataDef get_business_metadata_def_by_name(bm_name)

Read Business Metadata Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the business metadata definition with the given name.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.business_metadata_def import BusinessMetadataDef
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    bm_name = "bmName_example" # str | The name of the business metadata definition

    # example passing only required values which don't have defaults set
    try:
        # Read Business Metadata Definition
        api_response = api_instance.get_business_metadata_def_by_name(bm_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->get_business_metadata_def_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_name** | **str**| The name of the business metadata definition |

### Return type

[**BusinessMetadataDef**](BusinessMetadataDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definition |  -  |
**400** | Bad Request |  -  |
**404** | Business metadata definition not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_def_by_name**
> TagDef get_tag_def_by_name(tag_name)

Read Tag Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the tag definition with the given name.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.tag_def import TagDef
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    tag_name = "tagName_example" # str | The name of the tag definiton

    # example passing only required values which don't have defaults set
    try:
        # Read Tag Definition
        api_response = api_instance.get_tag_def_by_name(tag_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->get_tag_def_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag definiton |

### Return type

[**TagDef**](TagDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definition |  -  |
**400** | Bad Request |  -  |
**404** | Tag definition not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_metadata_defs**
> [BusinessMetadataDefResponse] update_business_metadata_defs()

Bulk Update Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk update API for business metadata definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.business_metadata_def_response import BusinessMetadataDefResponse
from openapi_client.model.business_metadata_def import BusinessMetadataDef
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    business_metadata_def = [
        BusinessMetadataDef(
            category="PRIMITIVE",
            guid="guid_example",
            created_by="created_by_example",
            updated_by="updated_by_example",
            create_time=1,
            update_time=1,
            version=1,
            name="name_example",
            description="description_example",
            type_version="type_version_example",
            service_type="service_type_example",
            options={
                "key": "key_example",
            },
            attribute_defs=[
                AttributeDef(
                    name="name_example",
                    type_name="type_name_example",
                    is_optional=True,
                    cardinality="SINGLE",
                    values_min_count=1,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="default_value_example",
                    description="description_example",
                    search_weight=1,
                    index_type="DEFAULT",
                    constraints=[
                        ConstraintDef(
                            type="type_example",
                            params={
                                "key": {},
                            },
                        ),
                    ],
                    options={
                        "key": "key_example",
                    },
                    display_name="display_name_example",
                ),
            ],
        ),
    ] # [BusinessMetadataDef] | The business metadata definitions to update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Update Business Metadata Definitions
        api_response = api_instance.update_business_metadata_defs(business_metadata_def=business_metadata_def)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->update_business_metadata_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata_def** | [**[BusinessMetadataDef]**](BusinessMetadataDef.md)| The business metadata definitions to update | [optional]

### Return type

[**[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions. Errored business metadata definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_defs**
> [TagDefResponse] update_tag_defs()

Bulk Update Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk update API for tag definitions.

### Example


```python
import time
import openapi_client
from openapi_client.api import types__v1_api
from openapi_client.model.tag_def import TagDef
from openapi_client.model.tag_def_response import TagDefResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types__v1_api.TypesV1Api(api_client)
    tag_def = [
        TagDef(
            category="PRIMITIVE",
            guid="guid_example",
            created_by="created_by_example",
            updated_by="updated_by_example",
            create_time=1,
            update_time=1,
            version=1,
            name="name_example",
            description="description_example",
            type_version="type_version_example",
            service_type="service_type_example",
            options={
                "key": "key_example",
            },
            attribute_defs=[
                AttributeDef(
                    name="name_example",
                    type_name="type_name_example",
                    is_optional=True,
                    cardinality="SINGLE",
                    values_min_count=1,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="default_value_example",
                    description="description_example",
                    search_weight=1,
                    index_type="DEFAULT",
                    constraints=[
                        ConstraintDef(
                            type="type_example",
                            params={
                                "key": {},
                            },
                        ),
                    ],
                    options={
                        "key": "key_example",
                    },
                    display_name="display_name_example",
                ),
            ],
            super_types=[
                "super_types_example",
            ],
            entity_types=[
                "entity_types_example",
            ],
            sub_types=[
                "sub_types_example",
            ],
        ),
    ] # [TagDef] | The tag definitions to update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk Update Tag Definitions
        api_response = api_instance.update_tag_defs(tag_def=tag_def)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesV1Api->update_tag_defs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_def** | [**[TagDef]**](TagDef.md)| The tag definitions to update | [optional]

### Return type

[**[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions. Errored tag definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

