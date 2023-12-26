# ServiceQuotaV1AppliedQuota

A `quota` object represents a quota configuration for a specific Confluent Cloud resource. Use this API to retrieve an individual quota or list of quotas for a given scope.   Related guide: [Service Quotas for Confluent Cloud](https://docs.confluent.io/cloud/current/quotas/index.html).  ## The Applied Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/service-quota.v1.AppliedQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "service-quota/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "AppliedQuota"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**scope** | **str** | The applied scope that this quota belongs to. | [optional] 
**display_name** | **str** | A human-readable name for the quota type name. | [optional] 
**default_limit** | **int** | The default service quota value.  | [optional] 
**applied_limit** | **int** | The latest applied service quota value, taking into account any limit adjustments.  | [optional] 
**usage** | **int** | Show the quota usage value if the quota usage is available for this quota.  | [optional] 
**user** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user associated with this object. | [optional] 
**organization** | **bool, date, datetime, dict, float, int, list, str, none_type** | A unique organization id to associate a specific organization to this quota. | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment ID the quota is associated with.  | [optional] 
**network** | **bool, date, datetime, dict, float, int, list, str, none_type** | The network ID the quota is associated with.  | [optional] 
**kafka_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The kafka cluster ID the quota is associated with.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


