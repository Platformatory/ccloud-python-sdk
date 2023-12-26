# ConsumerGroupLagSummaryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**max_lag_consumer_id** | **str** |  | 
**max_lag_client_id** | **str** |  | 
**max_lag_topic_name** | **str** |  | 
**max_lag_partition_id** | **int** |  | 
**max_lag** | **int** |  | 
**total_lag** | **int** |  | 
**max_lag_consumer** | [**Relationship**](Relationship.md) |  | 
**max_lag_partition** | [**Relationship**](Relationship.md) |  | 
**max_lag_instance_id** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


