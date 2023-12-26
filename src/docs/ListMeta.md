# ListMeta

ListMeta describes metadata that resource collections may have

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str, none_type** | A link to the first page of results. If a response does not contain a first link, then direct navigation to the first page is not supported. | [optional] 
**last** | **str, none_type** | A link to the last page of results. If a response does not contain a last link, then direct navigation to the last page is not supported. | [optional] 
**prev** | **str, none_type** | A link to the previous page of results. If a response does not contain a prev link, then either there is no previous data or backwards traversal through the result set is not supported. | [optional] 
**next** | **str, none_type** | A link to the next page of results. If a response does not contain a next link, then there is no more data available. | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


