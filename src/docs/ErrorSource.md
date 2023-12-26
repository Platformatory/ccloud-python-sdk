# ErrorSource

If this error was caused by a particular part of the API request, the source will point to the query string parameter or request body property that caused it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pointer** | **str** | A JSON Pointer [RFC6901] to the associated entity in the request document [e.g. \&quot;/spec\&quot; for a spec object, or \&quot;/spec/title\&quot; for a specific field]. | [optional] 
**parameter** | **str** | A string indicating which query parameter caused the error. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


