# IamV2ApiKeyList

`ApiKey` objects represent access to different parts of Confluent Cloud. Some types of API keys represent access to a single cluster/resource such as a Kafka cluster, Schema Registry cluster or a ksqlDB cluster. Cloud API Keys represent access to resources within an organization that are not tied to a specific cluster, such as the Org API, IAM API, Metrics API or Connect API.  The API allows you to list, create, update and delete your API Keys.   Related guide: [API Keys in Confluent Cloud](https://docs.confluent.io/cloud/current/client-apps/api-keys.html).  ## The API Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ApiKey\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `apikeys_per_org` | API Keys in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ApiKeyList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


