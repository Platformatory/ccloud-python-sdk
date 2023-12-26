# NetworkingV1AwsPrivateLinkAttachmentConnectionStatus

Status of a connection to an AWS PrivateLink attachment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_endpoint_service_name** | **str** | Id of the VPC Endpoint service used for PrivateLink. | [readonly] 
**vpc_endpoint_id** | **str** | Id of the VPC Endpoint (if any) that is connected to the VPC Endpoint service. | [readonly] 
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | defaults to "AwsPrivateLinkAttachmentConnectionStatus"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


