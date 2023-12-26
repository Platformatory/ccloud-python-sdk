# IamV2InvitationList

`Invitation` objects represent invitations to invite users to join your organizations in Confluent Cloud.  The API allows you to list all your invitations, as well as create, read, and delete a specified invitation.   Related guide: [User invitations in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/identity/user-accounts.html).  ## The Invitations Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.Invitation\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `invitations_per_org` | Invitations in a Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "InvitationList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


