# NetworkingV1TransitGatewayAttachmentStatus

The status of the Transit Gateway Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the TGW attachment:    PROVISIONING: attachment provisioning is in progress;    PENDING_ACCEPT: attachment request is pending acceptance by the customer;    READY:  attachment is ready;    FAILED: attachment is in a failed state;    DEPROVISIONING: attachment deprovisioning is in progress;    DISCONNECTED: attachment was manually deleted directly in the cloud provider by the customer;    ERROR: invalid customer input during attachment creation.  | [readonly] 
**error_code** | **str** | Error code if TGW attachment is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if TGW attachment is in a failed state | [optional] [readonly] 
**cloud** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The cloud-specific TGW attachment details. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


