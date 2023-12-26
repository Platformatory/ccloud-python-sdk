# NetworkingV1PrivateLinkAttachmentConnection

PrivateLink attachment connection objects represent connections established to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachment connections.   ## The Private Link Attachment Connections Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachmentConnection\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "PrivateLinkAttachmentConnection"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**NetworkingV1PrivateLinkAttachmentConnectionSpec**](NetworkingV1PrivateLinkAttachmentConnectionSpec.md) |  | [optional] 
**status** | [**NetworkingV1PrivateLinkAttachmentConnectionStatus**](NetworkingV1PrivateLinkAttachmentConnectionStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


