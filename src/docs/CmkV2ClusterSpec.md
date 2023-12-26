# CmkV2ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the cluster. | [optional] 
**availability** | **str** | The availability zone configuration of the cluster  | [optional] 
**cloud** | **str** | The cloud service provider in which the cluster is running. | [optional] 
**region** | **str** | The cloud service provider region where the cluster is running. | [optional] 
**config** | **bool, date, datetime, dict, float, int, list, str, none_type** | The configuration of the Kafka cluster.  Note: Clusters can be upgraded from Basic to Standard, but cannot be downgraded from Standard to Basic.  | [optional] 
**kafka_bootstrap_endpoint** | **str** | The bootstrap endpoint used by Kafka clients to connect to the cluster. | [optional] [readonly] 
**http_endpoint** | **str** | The cluster HTTP request URL. | [optional] [readonly] 
**api_endpoint** | **str** | The Kafka API cluster endpoint used by Kafka clients to connect to the cluster. | [optional] [readonly] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**network** | **bool, date, datetime, dict, float, int, list, str, none_type** | The network associated with this object. | [optional] 
**byok** | **bool, date, datetime, dict, float, int, list, str, none_type** | The byok associated with this object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


