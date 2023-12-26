# KafkaQuotasV1ClientQuotaSpecUpdate

The desired state of the Client Quota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the client quota. | [optional] 
**description** | **str** | A human readable description for the client quota. | [optional] 
**throughput** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Throughput for the client quota. | [optional] 
**principals** | [**[GlobalObjectReference]**](GlobalObjectReference.md) | A list of principals to apply a client quota to. Use &#x60;\&quot;&lt;default&gt;\&quot;&#x60; to apply a client quota to all service accounts (see [Control application usage with Client Quotas](https://docs.confluent.io/cloud/current/clusters/client-quotas.html#control-application-usage-with-client-quotas) for more details).  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


