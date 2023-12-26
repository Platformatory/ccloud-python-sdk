# CmkV2ClusterStatus

The status of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecyle phase of the cluster:   PROVISIONED:  cluster is provisioned;   PROVISIONING:  cluster provisioning is in progress;   FAILED:  provisioning failed  | [readonly] 
**cku** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of Confluent Kafka Units (CKUs) the Dedicated cluster currently has.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


