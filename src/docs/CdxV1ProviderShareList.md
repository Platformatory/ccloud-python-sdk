# CdxV1ProviderShareList

`ProviderShare` object respresents the share that you have created through Stream Sharing.   Related guide: [Provider Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/produce-shared-data.html#stream-shares).  ## The Provider Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ProviderShareList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


