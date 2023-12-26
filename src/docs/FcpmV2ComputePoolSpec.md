# FcpmV2ComputePoolSpec

The desired state of the Compute Pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Flink compute pool. | [optional] 
**cloud** | **str** | The cloud service provider that runs the compute pool. | [optional] 
**http_endpoint** | **str** | The API endpoint of the Flink compute pool. | [optional] [readonly] 
**region** | **str** | Flink compute pools in the region provided will be able to use this identity pool | [optional] 
**max_cfu** | **int** | Maximum number of Confluent Flink Units (CFUs) that the Flink compute pool should auto-scale to.  | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**network** | **bool, date, datetime, dict, float, int, list, str, none_type** | The network to which this belongs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


