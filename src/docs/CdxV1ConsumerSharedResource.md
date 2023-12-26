# CdxV1ConsumerSharedResource

`ConsumerSharedResource` object contains details of the data stream (topic, schema registry subjects, sharing metadata) that you received through Stream Sharing.   ## The Consumer Shared Resources Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ConsumerSharedResource\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "ConsumerSharedResource"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**cloud** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**network_connection_types** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**display_name** | **str** | Consumer resource display name | [optional] [readonly] 
**description** | **str** | Description of consumer resource | [optional] [readonly] 
**tags** | **[str]** | list of tags | [optional] [readonly] 
**schemas** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of schemas in JSON format. This field is work in progress and subject to changes. | [optional] [readonly] 
**organization_name** | **str** | Shared resource&#39;s organization name | [optional] [readonly] 
**organization_description** | **str** | Shared resource&#39;s organization description | [optional] [readonly] 
**organization_contact** | **str** | Email of the shared resource&#39;s organization contact | [optional] [readonly] 
**logo_url** | **str** | Resource logo url | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


