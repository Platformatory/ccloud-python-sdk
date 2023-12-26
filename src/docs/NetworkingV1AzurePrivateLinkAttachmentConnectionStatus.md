# NetworkingV1AzurePrivateLinkAttachmentConnectionStatus

Status of an Azure PrivateLink attachment connection for an availability zone.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | Availability zone associated with the Azure PrivateLink service. | [readonly] 
**private_link_service_alias** | **str** | Azure PrivateLink service alias for the availability zone. | [readonly] 
**private_link_service_resource_id** | **str** | Azure PrivateLink service resource id for the availability zone. | [readonly] 
**private_endpoint_resource_id** | **str** | Resource Id of the PrivateEndpoint (if any) that is connected to the PrivateLink service for this availability zone.  | [readonly] 
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | defaults to "AzurePrivateLinkAttachmentConnectionStatus"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


