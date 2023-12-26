# NetworkingV1AzureNetwork

The Azure network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnet** | **str** | The resource ID of the Confluent Cloud VNet. | [readonly] 
**subscription** | **str** | The Azure Subscription ID associated with the Confluent Cloud VPC. | [readonly] 
**kind** | **str** | Network kind type. | defaults to "AzureNetwork"
**private_link_service_aliases** | **{str: (str,)}** | The mapping of zones to Private Link Service Aliases if available. Keys are zones and values are [Azure Private Link Service Aliases](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 
**private_link_service_resource_ids** | **{str: (str,)}** | The mapping of zones to Private Link Service Resource IDs if available. Keys are zones and values are [Azure Private Link Service Resource IDs](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


