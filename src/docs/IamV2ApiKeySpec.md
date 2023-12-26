# IamV2ApiKeySpec

The desired state of the Api Key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The API key secret. Only provided in &#x60;create&#x60; responses, not in &#x60;get&#x60; or &#x60;list&#x60;. | [optional] [readonly] 
**display_name** | **str** | A human readable name for the API key | [optional] 
**description** | **str** | A human readable description for the API key | [optional] 
**owner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The owner to which this belongs. The owner can be one of iam.v2.User, iam.v2.ServiceAccount. | [optional] 
**resource** | **bool, date, datetime, dict, float, int, list, str, none_type** | The resource associated with this object. The resource can be one of Kafka Cluster ID (example: lkc-12345), Schema Registry Cluster ID (example: lsrc-12345), ksqlDB Cluster ID (example: lksqlc-12345), or Flink (Environment + Region pair, example: env-abc123.aws.us-east-2). May be null or omitted if not associated with a resource. For Cloud API keys, resource should be &#x60;null&#x60;. [Learn more in Authentication](https://docs.confluent.io/cloud/current/api.html#section/Authentication).  Note - Flink is in the [Preview lifecycle stage](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


