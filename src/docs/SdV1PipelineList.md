# SdV1PipelineList

`Pipeline` objects represent information about a user-defined pipeline of Confluent Cloud components. The pipeline's content is available separately.  The API allows you to create, retrieve, update, and delete your pipelines, as well as list all of your pipelines for the particular environment and Kafka cluster.   Related guide: [Pipelines in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-designer/).  ## The Pipelines Model <SchemaDefinition schemaRef=\"#/components/schemas/sd.v1.Pipeline\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `pipelines_per_org` | Pipelines in one Confluent Cloud organization | | `pipelines_per_cluster` | Pipelines in one Confluent Cloud Kafka cluster |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "sd/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "PipelineList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


