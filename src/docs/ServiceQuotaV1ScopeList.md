# ServiceQuotaV1ScopeList

Gets a list of all available scopes for applied quotas.   Related guide: [Quota Scopes](https://docs.confluent.io/cloud/current/quotas/quotas.html#query-for-scopes).  ## The Scopes Model <SchemaDefinition schemaRef=\"#/components/schemas/service-quota.v1.Scope\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "service-quota/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ScopeList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


