# OrgV2OrganizationList

`Organization` objects represent a customer organization. An organization contains all customer resources (e.g., Environments, Kafka Clusters, Service Accounts, API Keys) and is tied to a billing agreement (including any annual commitment or support plan).  The API allows you to list, view, and update your organizations.   Related guide: [Organizations for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/hierarchy/organizations/cloud-organization.html).  ## The Organizations Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Organization\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `organizations_per_user` | Confluent Cloud organizations a user belongs to |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "org/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "OrganizationList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


