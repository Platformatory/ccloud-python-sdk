# FcpmV2ComputePoolList

A Compute Pool represents a set of compute resources that is used to run your Queries. The resources (CPUs, memory,…) provided by a Compute Pool are shared between all Queries that use it.   ## The Compute Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/fcpm.v2.ComputePool\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "fcpm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ComputePoolList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


