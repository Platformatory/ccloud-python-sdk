# IamV2ServiceAccountList

`ServiceAccount` objects are typically used to represent applications and other non-human principals that may access your Confluent resources.  The API allows you to create, retrieve, update, and delete individual service accounts, as well as list all your service accounts.   Related guide: [Service Accounts in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/service-account.html).  ## The Service Accounts Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ServiceAccount\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `service_accounts_per_org` | Service Accounts in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ServiceAccountList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


