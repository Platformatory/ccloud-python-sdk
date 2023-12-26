# SdV1Pipeline

`Pipeline` objects represent information about a user-defined pipeline of Confluent Cloud components. The pipeline's content is available separately.  The API allows you to create, retrieve, update, and delete your pipelines, as well as list all of your pipelines for the particular environment and Kafka cluster.   Related guide: [Pipelines in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-designer/).  ## The Pipelines Model <SchemaDefinition schemaRef=\"#/components/schemas/sd.v1.Pipeline\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `pipelines_per_org` | Pipelines in one Confluent Cloud organization | | `pipelines_per_cluster` | Pipelines in one Confluent Cloud Kafka cluster |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "sd/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Pipeline"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**SdV1PipelineSpec**](SdV1PipelineSpec.md) |  | [optional] 
**status** | [**SdV1PipelineStatus**](SdV1PipelineStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


