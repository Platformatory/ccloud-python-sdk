# ReplicaStatusData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**broker_id** | **int** |  | 
**partition_id** | **int** |  | 
**is_leader** | **bool** |  | 
**is_observer** | **bool** |  | 
**is_isr_eligible** | **bool** |  | 
**is_in_isr** | **bool** |  | 
**is_caught_up** | **bool** |  | 
**log_start_offset** | **int** |  | 
**log_end_offset** | **int** |  | 
**last_caught_up_time_ms** | **int** |  | 
**last_fetch_time_ms** | **int** |  | 
**link_name** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


