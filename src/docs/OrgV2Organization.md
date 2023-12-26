# OrgV2Organization

`Organization` objects represent a customer organization. An organization contains all customer resources (e.g., Environments, Kafka Clusters, Service Accounts, API Keys) and is tied to a billing agreement (including any annual commitment or support plan).  The API allows you to list, view, and update your organizations.   Related guide: [Organizations for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/hierarchy/organizations/cloud-organization.html).  ## The Organizations Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Organization\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `organizations_per_user` | Confluent Cloud organizations a user belongs to |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "org/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Organization"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**display_name** | **str** | A human-readable name for the Organization | [optional] 
**jit_enabled** | **bool** | The flag to toggle Just-In-Time user provisioning for SSO-enabled organization. Available for early access only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


