# FcpmV2Region

`Region` objects represent cloud provider regions available when placing Flink compute pools. The API allows you to list Flink regions.   ## The Regions Model <SchemaDefinition schemaRef=\"#/components/schemas/fcpm.v2.Region\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "fcpm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Region"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**display_name** | **str** | The display name. | [optional] [readonly] 
**cloud** | **str** | The cloud service provider that hosts the region. | [optional] [readonly] 
**region_name** | **str** | The region name. | [optional] [readonly] 
**http_endpoint** | **str** | The regional API endpoint for flink compute pools. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


