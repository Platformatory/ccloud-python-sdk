# SrcmV2Region

`Region` objects represent cloud provider regions available when placing Schema Registry clusters. The API allows you to list Schema Registry regions.   Related guide: [Confluent Cloud Schema Registry Regions](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-regions).  ## The Regions Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v2.Region\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "srcm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Region"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**SrcmV2RegionSpec**](SrcmV2RegionSpec.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


