# NetworkingV1GcpPrivateLinkAttachmentStatus

GCP PrivateLink attachment represents reserved capacity in zonal GCP PSC Service attachments.  A PSC Endpoint can be connected to the Service attachment corresponding to each zone. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_attachments** | [**[NetworkingV1GcpPscServiceAttachment]**](NetworkingV1GcpPscServiceAttachment.md) | Array of GCP PSC Service attachments that can be used to connect PSC Endpoints for each zone.  | [readonly] 
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] defaults to "GcpPrivateLinkAttachmentStatus"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


