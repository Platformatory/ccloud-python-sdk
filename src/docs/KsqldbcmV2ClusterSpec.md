# KsqldbcmV2ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the ksqlDB cluster. | [optional] 
**use_detailed_processing_log** | **bool** | This flag controls whether you want to include the row data in the processing log topic. Turn it off if you don&#39;t want to emit sensitive information to the processing log  | [optional]  if omitted the server will use the default value of True
**csu** | **int** | The number of CSUs (Confluent Streaming Units) in a ksqlDB cluster. | [optional] 
**kafka_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The kafka_cluster to which this belongs. | [optional] 
**credential_identity** | **bool, date, datetime, dict, float, int, list, str, none_type** | The credential_identity to which this belongs. The credential_identity can be one of iam.v2.User, iam.v2.ServiceAccount. | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


