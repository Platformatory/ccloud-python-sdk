# IamV2SsoGroupMapping

`GroupMapping` objects establish relationships between user groups in your SSO identity provider and specific RBAC roles in Confluent Cloud.  Group mappings enable automated and secure access control to Confluent Cloud resources, reducing administrative workload by streamlining user provisioning and authorization.   Related guide: [Use group mappings with your SSO identity provider](https://docs.confluent.io/cloud/current/access-management/authenticate/sso/group-mapping/overview.html).  ## The Group Mappings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.sso.GroupMapping\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `group_mappings_per_org` | Number of group mappings per organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "iam.v2/sso"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "GroupMapping"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**display_name** | **str** | The name of the group mapping. | [optional] 
**description** | **str** | A description explaining the purpose and use of the group mapping. | [optional] 
**filter** | **str** | A single group identifier or a condition based on [supported CEL operators](https://docs.confluent.io/cloud/current/access-management/authenticate/sso/group-mapping/overview.html#supported-cel-operators-for-group-mapping) that defines which groups are included. | [optional] 
**principal** | **str** | The unique federated identity associated with this group mapping. | [optional] [readonly] 
**state** | **str** | The current state of the group mapping. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


