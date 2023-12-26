# CmkV2ClusterUpdate

`Clusters` objects represent Apache Kafka Clusters on Confluent Cloud.  The API allows you to list, create, read, update, and delete your Kafka clusters.   Related guide: [Confluent Cloud Cluster Management for Apache Kafka APIs](https://docs.confluent.io/cloud/current/clusters/cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/cmk.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `kafka_clusters_per_environment` | Number of clusters in one Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cmk/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Cluster"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**CmkV2ClusterSpecUpdate**](CmkV2ClusterSpecUpdate.md) |  | [optional] 
**status** | [**CmkV2ClusterStatus**](CmkV2ClusterStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


