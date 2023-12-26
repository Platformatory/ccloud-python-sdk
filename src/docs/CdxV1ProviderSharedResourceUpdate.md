# CdxV1ProviderSharedResourceUpdate

`ProviderSharedResource` object contains details of the data stream (topic, schema registry subjects, sharing metadata) that you have shared through Stream Sharing.   ## The Provider Shared Resources Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderSharedResource\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "ProviderSharedResource"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**resources** | **[str]** | List of resource crns that are shared together | [optional] 
**display_name** | **str** | Shared resource display name | [optional] 
**organization_description** | **str** | Shared resource&#39;s organization description | [optional] 
**organization_contact** | **str** | Email of contact person from the organization | [optional] 
**logo_url** | **str** | Resource logo url | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


