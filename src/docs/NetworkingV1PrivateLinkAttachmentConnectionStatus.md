# NetworkingV1PrivateLinkAttachmentConnectionStatus

The status of the Private Link Attachment Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink attachment:    PROVISIONING: PrivateLink attachment connection provisioning is in progress;    READY: PrivateLink attachment connection is ready;    FAILED: PrivateLink attachment connection is in a failed state;    DEPROVISIONING: PrivateLink attachment connection deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink attachment connection is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink attachment connection is in a failed state. | [optional] [readonly] 
**cloud** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The cloud specific status of the PrivateLink attachment connection. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


