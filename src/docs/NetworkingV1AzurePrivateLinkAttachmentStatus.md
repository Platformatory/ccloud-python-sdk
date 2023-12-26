# NetworkingV1AzurePrivateLinkAttachmentStatus

Azure PrivateLink attachment represents reserved capacity in zonal PrivateLink services.  A Private Endpoint can be connected to the PLS corresponding to each zone. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_link_services** | [**[NetworkingV1AzurePrivateLinkService]**](NetworkingV1AzurePrivateLinkService.md) | Array of Azure PrivateLink services that can be used to connect PrivateEndpoints for each availability zone.  | [readonly] 
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] defaults to "AzurePrivateLinkAttachmentStatus"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


