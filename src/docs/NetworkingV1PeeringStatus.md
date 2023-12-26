# NetworkingV1PeeringStatus

The status of the Peering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the peering:    PROVISIONING: peering provisioning is in progress;    PENDING_ACCEPT: peering connection request is pending acceptance by the customer;    READY:  peering is ready;    FAILED: peering is in a failed state;    DEPROVISIONING: peering deprovisioning is in progress;    DISCONNECTED: peering has been disconnected in the cloud provider by the customer;  | [readonly] 
**error_code** | **str** | Error code if peering is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if peering is in a failed state | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


