# SqlV1beta1StatementSpec

The specs of the Statement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | **str** | The raw SQL text statement. | [optional] 
**properties** | **{str: (str,)}** | A map (key-value pairs) of statement properties. | [optional] 
**compute_pool_id** | **str** | The id associated with the compute pool in context. | [optional] 
**principal** | **str** | The id of a principal this statement runs as. | [optional] 
**stopped** | **bool** | Indicates whether the statement should be stopped. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


