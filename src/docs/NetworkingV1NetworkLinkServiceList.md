# NetworkingV1NetworkLinkServiceList

Network Link Service is associated with a Private Link Confluent Cloud Network. It enables connectivity from other Private Link Confluent Cloud Networks based on the configured accept policies.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Services Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkService\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `network_link_service_per_network` | Number of network link services per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "NetworkLinkServiceList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


