# NetworkingV1PrivateLinkAccessStatus

The status of the Private Link Access

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink access configuration:    PROVISIONING: PrivateLink access provisioning is in progress;    READY:  PrivateLink access is ready;    FAILED: PrivateLink access is in a failed state;    DEPROVISIONING: PrivateLink access deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink access is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink access is in a failed state | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


