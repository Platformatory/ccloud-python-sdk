# SqlV1beta1ScalingStatus

Scaling status for this statement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scaling_state** | **str** | OK: The statement runs at the right scale. PENDING_SCALE_DOWN: The statement requires less resources, and will be scaled down in the near future. PENDING_SCALE_UP: The statement requires more resources, and will be scaled up in the near future. POOL_EXHAUSTED: The statement requires more resources, but not enough resources are available.  | [optional] [readonly] 
**last_updated** | **datetime** | The last time the scaling status was updated. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


