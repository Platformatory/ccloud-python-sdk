# SrcmV2RegionList

`Region` objects represent cloud provider regions available when placing Schema Registry clusters. The API allows you to list Schema Registry regions.   Related guide: [Confluent Cloud Schema Registry Regions](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-regions).  ## The Regions Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v2.Region\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "srcm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "RegionList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


