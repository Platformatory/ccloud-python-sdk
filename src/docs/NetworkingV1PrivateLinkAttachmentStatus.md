# NetworkingV1PrivateLinkAttachmentStatus

The status of the Private Link Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink attachment:    PROVISIONING: PrivateLink attachment provisioning is in progress;    WAITING_FOR_CONNECTIONS: PrivateLink attachment is waiting for connections;    READY: PrivateLink attachment is ready;    FAILED: PrivateLink attachment is in a failed state;    EXPIRED: PrivateLink attachment has timed out waiting for connections, can only be deleted;    DEPROVISIONING: PrivateLink attachment deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink attachment is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink attachment is in a failed state. | [optional] [readonly] 
**dns_domain** | **str** | The root DNS domain for the PrivateLink attachment. | [optional] [readonly] 
**cloud** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The cloud specific status of the PrivateLink attachment. These will be populated when the PrivateLink attachment reaches the WAITING_FOR_CONNECTIONS state. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


