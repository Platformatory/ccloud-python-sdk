# SdV1PipelineSpec

The desired state of the Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the pipeline. | [optional] 
**description** | **str** | The description of the pipeline. | [optional] 
**retained_topic_names** | **[str]** | A list of Kafka topic names from the activated pipeline to be retained when this pipeline is deactivated.  | [optional] 
**activated** | **bool** | The desired state of the pipeline. | [optional]  if omitted the server will use the default value of False
**activation_privilege** | **bool** | Whether the pipeline has privileges to be activated. | [optional]  if omitted the server will use the default value of False
**source_code** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A map of source code format and statements that define this pipeline. | [optional] 
**secrets** | **{str: (str,)}** | A map of secrets used in the pipeline source code. | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**kafka_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The kafka_cluster to which this belongs. | [optional] 
**ksql_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ksql_cluster associated with this object. | [optional] 
**stream_governance_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The stream_governance_cluster associated with this object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


