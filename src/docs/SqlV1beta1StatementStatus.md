# SqlV1beta1StatementStatus

The status of the Statement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the submitted SQL statement: PENDING: SQL statement is pending execution; RUNNING: SQL statement execution is in progress; COMPLETED: SQL statement is completed; DELETING: SQL statement deletion is in progress; FAILING: SQL statement is failing; FAILED: SQL statement execution has failed; STOPPED: SQL statement execution has successfully been stopped;  | [readonly] 
**scaling_status** | [**SqlV1beta1ScalingStatus**](SqlV1beta1ScalingStatus.md) |  | [optional] 
**result_schema** | [**SqlV1beta1ResultSchema**](SqlV1beta1ResultSchema.md) |  | [optional] 
**detail** | **str** | Description of a SQL statement phase. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


