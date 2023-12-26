# KsqldbcmV2Cluster

`Cluster` represents a ksqlDB runtime that you can issue queries to using its API endpoint. It executes SQL statements and queries which under the hood get built into corresponding Kafka Streams topologies. The API allows you to list, create, read, and delete your ksqlDB clusters.   Related guide: [ksqlDB in Confluent Cloud](https://docs.confluent.io/cloud/current/ksqldb/ksqldb-cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/ksqldbcm.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `ksql.limits.max_apps_per_cluster` | Clusters in one Confluent Cloud Kafka Cluster. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "ksqldbcm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Cluster"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**KsqldbcmV2ClusterSpec**](KsqldbcmV2ClusterSpec.md) |  | [optional] 
**status** | [**KsqldbcmV2ClusterStatus**](KsqldbcmV2ClusterStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


