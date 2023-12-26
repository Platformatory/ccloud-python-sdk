# CmkV2ClusterList

`Clusters` objects represent Apache Kafka Clusters on Confluent Cloud.  The API allows you to list, create, read, update, and delete your Kafka clusters.   Related guide: [Confluent Cloud Cluster Management for Apache Kafka APIs](https://docs.confluent.io/cloud/current/clusters/cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/cmk.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `kafka_clusters_per_environment` | Number of clusters in one Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "cmk/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ClusterList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


