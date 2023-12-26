# NetworkingV1PrivateLinkAttachmentList

PrivateLink attachment objects represent reservations to establish PrivateLink connections to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachments.   ## The Private Link Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `private_link_attachments_per_environment` | Number of PrivateLink Attachments per environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "PrivateLinkAttachmentList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


