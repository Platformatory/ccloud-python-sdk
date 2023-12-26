# NetworkingV1GcpPrivateLinkAttachmentConnectionStatus

Status of a GCP PrivateLink attachment connection for a zone.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | Zone associated with the GCP PrivateLink attachment connection. | [readonly] 
**private_service_connect_service_attachment** | **str** | GCP Private Service Connect ServiceAttachment for the zone. | [readonly] 
**private_service_connect_connection_id** | **str** | Id of the Private Service connection. | [readonly] 
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | defaults to "GcpPrivateLinkAttachmentConnectionStatus"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


