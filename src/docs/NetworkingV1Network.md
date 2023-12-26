# NetworkingV1Network

`Network` represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider accounts. Dedicated networks support more networking options but can only contain Dedicated clusters. Shared networks can contain any cluster type.  The API allows you to list, create, read, update, and delete your networks.   Related guide: [APIs to manage networks in Confluent Cloud](https://docs.confluent.io/cloud/current/networking/overview.html).  ## The Networks Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Network\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `dedicated_networks_per_environment` | Number of dedicated networks per Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Network"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**NetworkingV1NetworkSpec**](NetworkingV1NetworkSpec.md) |  | [optional] 
**status** | [**NetworkingV1NetworkStatus**](NetworkingV1NetworkStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


