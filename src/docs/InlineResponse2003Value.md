# InlineResponse2003Value

The current value for a config, which includes the name, value, recommended values, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | [optional] 
**value** | **str** | The value for the configuration | [optional] 
**recommended_values** | **[str]** | The list of valid values for the configuration | [optional] 
**errors** | **[str]** | Errors, if any, in the configuration value | [optional] 
**visible** | **bool** | The visibility of the configuration. Based on the values of other configuration fields, this visibility boolean value points out if the current field should be visible or not. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


