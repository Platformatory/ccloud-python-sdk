# ByokV1AzureKey

The Azure BYOK details. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The unique Key Object Identifier URL without version of an Azure Key Vault key.  | 
**key_vault_id** | **str** | Key Vault ID containing the key  | 
**tenant_id** | **str** | Tenant ID (uuid) hosting the Key Vault containing the key  | 
**kind** | **str** | BYOK kind type.  | defaults to "AzureKey"
**application_id** | **str** | The Application ID created for this key-environment combination.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


