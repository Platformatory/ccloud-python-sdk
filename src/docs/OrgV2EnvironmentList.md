# OrgV2EnvironmentList

`Environment` objects represent an isolated namespace for your Confluent resources for organizational purposes.  The API allows you to create, delete, and update your environments. You can retrieve individual environments as well as a list of all your environments.   Related guide: [Environments in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/environments.html).  ## The Environments Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Environment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `environments_per_org` | Environments in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "org/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "EnvironmentList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


