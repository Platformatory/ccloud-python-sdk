# SdV1PipelineStatus

The status of the Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The current state of the pipeline.:   DRAFT:  the pipeline is a draft and not activated yet;   ACTIVATING:  the pipeline activation is in progress;   DEACTIVATING:  the pipeline deactivation is in progress;   ACTIVE:  the pipeline is actived and running;   FAILED:  the pipeline activation or deactivation failed;   DELETED:  the pipeline is deleted  | [optional] [readonly] 
**topic_count** | **int** | The number of Kafka topics defined in the pipeline. | [optional] [readonly] 
**connector_count** | **int** | The number of connectors defined in the pipeline. | [optional] [readonly] 
**query_count** | **int** | The number of KSQL queries defined in the pipeline. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


