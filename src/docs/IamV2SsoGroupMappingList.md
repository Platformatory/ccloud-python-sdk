# IamV2SsoGroupMappingList

`GroupMapping` objects establish relationships between user groups in your SSO identity provider and specific RBAC roles in Confluent Cloud.  Group mappings enable automated and secure access control to Confluent Cloud resources, reducing administrative workload by streamlining user provisioning and authorization.   Related guide: [Use group mappings with your SSO identity provider](https://docs.confluent.io/cloud/current/access-management/authenticate/sso/group-mapping/overview.html).  ## The Group Mappings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.sso.GroupMapping\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `group_mappings_per_org` | Number of group mappings per organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam.v2/sso"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "GroupMappingList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


