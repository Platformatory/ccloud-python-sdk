# ByokV1KeyList

`Key` objects represent customer managed keys on dedicated Confluent Cloud clusters.  Keys are used to protect data at rest stored in your dedicated Confluent Cloud clusters on AWS, Azure, and GCP. This API allows you to upload and retrieve self-managed keys on Confluent Cloud.   Related guide: [Confluent Cloud Bring Your Own Key (BYOK) Management API](https://docs.confluent.io/cloud/current/clusters/byok/index.html).  ## The Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/byok.v1.Key\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `byok.max_keys.per_org` | BYOK keys in one Confluent Cloud organisation. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "byok/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "KeyList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


