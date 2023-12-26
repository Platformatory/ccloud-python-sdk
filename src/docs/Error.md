# Error

Describes a particular error encountered while performing an operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this particular occurrence of the problem. | [optional] 
**status** | **str** | The HTTP status code applicable to this problem, expressed as a string value. | [optional] 
**code** | **str** | An application-specific error code, expressed as a string value. | [optional] 
**title** | **str** | A short, human-readable summary of the problem. It **SHOULD NOT** change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**error_code** | **int** |  | [optional] 
**message** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


