# ConfigUpdateRequest

Config update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | If alias is specified, then this subject is an alias for the subject named by the alias. That means that any reference to this subject will be replaced by the alias. | [optional] 
**normalize** | **bool** | If true, then schemas are automatically normalized when registered or when passed during lookups. This means that clients do not have to pass the \&quot;normalize\&quot; query parameter to have normalization occur. | [optional] 
**compatibility** | **str** | Compatibility Level | [optional] 
**compatibility_group** | **str** | Only schemas that belong to the same compatibility group will be checked for compatibility. | [optional] 
**default_metadata** | [**ConfigDefaultMetadata**](ConfigDefaultMetadata.md) |  | [optional] 
**override_metadata** | [**ConfigOverrideMetadata**](ConfigOverrideMetadata.md) |  | [optional] 
**default_rule_set** | [**ConfigDefaultRuleSet**](ConfigDefaultRuleSet.md) |  | [optional] 
**override_rule_set** | [**ConfigOverrideRuleSet**](ConfigOverrideRuleSet.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


