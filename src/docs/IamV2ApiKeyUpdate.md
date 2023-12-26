# IamV2ApiKeyUpdate

`ApiKey` objects represent access to different parts of Confluent Cloud. Some types of API keys represent access to a single cluster/resource such as a Kafka cluster, Schema Registry cluster or a ksqlDB cluster. Cloud API Keys represent access to resources within an organization that are not tied to a specific cluster, such as the Org API, IAM API, Metrics API or Connect API.  The API allows you to list, create, update and delete your API Keys.   Related guide: [API Keys in Confluent Cloud](https://docs.confluent.io/cloud/current/client-apps/api-keys.html).  ## The API Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ApiKey\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `apikeys_per_org` | API Keys in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "ApiKey"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**IamV2ApiKeySpecUpdate**](IamV2ApiKeySpecUpdate.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


