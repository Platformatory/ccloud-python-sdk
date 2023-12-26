# InlineResponse2003Definition

The definition for a config in the connector plugin, which includes the name, type, importance, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | [optional] 
**type** | **str** | The config types | [optional] 
**required** | **bool** | Whether this configuration is required | [optional] 
**default_value** | **str** | Default value for this configuration | [optional] 
**importance** | **str** | The importance level for a configuration | [optional] 
**documentation** | **str** | The documentation for the configuration | [optional] 
**group** | **str** | The UI group to which the configuration belongs to | [optional] 
**width** | **str** | The width of a configuration value | [optional] 
**display_name** | **str** |  | [optional] 
**dependents** | **[str]** | Other configurations on which this configuration is dependent | [optional] 
**order** | **int** | The order of configuration in specified group | [optional] 
**alias** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


