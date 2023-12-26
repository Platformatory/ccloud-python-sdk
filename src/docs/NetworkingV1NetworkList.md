# NetworkingV1NetworkList

`Network` represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider accounts. Dedicated networks support more networking options but can only contain Dedicated clusters. Shared networks can contain any cluster type.  The API allows you to list, create, read, update, and delete your networks.   Related guide: [APIs to manage networks in Confluent Cloud](https://docs.confluent.io/cloud/current/networking/overview.html).  ## The Networks Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Network\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `dedicated_networks_per_environment` | Number of dedicated networks per Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "NetworkList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


