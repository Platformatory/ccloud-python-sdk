# NetworkingV1PrivateLinkAttachmentConnectionList

PrivateLink attachment connection objects represent connections established to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachment connections.   ## The Private Link Attachment Connections Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachmentConnection\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "PrivateLinkAttachmentConnectionList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


