# BrokerTaskDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**task_type** | [**BrokerTaskType**](BrokerTaskType.md) |  | 
**task_status** | **str** |  | 
**sub_task_statuses** | **{str: (str,)}** |  | 
**created_at** | **datetime** | The date and time at which this task was created. | [readonly] 
**updated_at** | **datetime** | The date and time at which this task was last updated. | [readonly] 
**broker** | [**Relationship**](Relationship.md) |  | 
**shutdown_scheduled** | **bool, none_type** |  | [optional] 
**error_code** | **int, none_type** |  | [optional] 
**error_message** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


