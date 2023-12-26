# KsqldbcmV2ClusterStatus

The status of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Status of the ksqlDB cluster. | [readonly] 
**is_paused** | **bool** | Tells you if the cluster has been paused | [readonly] 
**storage** | **int** | Amount of storage (in GB) provisioned to this cluster | [readonly] 
**http_endpoint** | **str** | The dataplane endpoint of the ksqlDB cluster. | [optional] [readonly] 
**topic_prefix** | **str** | Topic name prefix used by this ksqlDB cluster. Used to assign ACLs for this ksqlDB cluster to use. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


