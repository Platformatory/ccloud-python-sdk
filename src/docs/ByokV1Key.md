# ByokV1Key

`Key` objects represent customer managed keys on dedicated Confluent Cloud clusters.  Keys are used to protect data at rest stored in your dedicated Confluent Cloud clusters on AWS, Azure, and GCP. This API allows you to upload and retrieve self-managed keys on Confluent Cloud.   Related guide: [Confluent Cloud Bring Your Own Key (BYOK) Management API](https://docs.confluent.io/cloud/current/clusters/byok/index.html).  ## The Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/byok.v1.Key\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `byok.max_keys.per_org` | BYOK keys in one Confluent Cloud organisation. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "byok/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Key"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**key** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The cloud-specific key details.  For AWS, provide the corresponding &#x60;key_arn&#x60;.  For Azure, provide the corresponding &#x60;key_id&#x60;.  For GCP, provide the corresponding &#x60;key_id&#x60;.  | [optional] 
**provider** | **str** | The cloud provider of the Key. | [optional] [readonly] 
**state** | **str** | The state of the key:   AVAILABLE: key can be used for a Kafka cluster provisioning   IN_USE: key is already in use by a Kafka cluster provisioning  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


