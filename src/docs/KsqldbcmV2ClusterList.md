# KsqldbcmV2ClusterList

`Cluster` represents a ksqlDB runtime that you can issue queries to using its API endpoint. It executes SQL statements and queries which under the hood get built into corresponding Kafka Streams topologies. The API allows you to list, create, read, and delete your ksqlDB clusters.   Related guide: [ksqlDB in Confluent Cloud](https://docs.confluent.io/cloud/current/ksqldb/ksqldb-cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/ksqldbcm.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `ksql.limits.max_apps_per_cluster` | Clusters in one Confluent Cloud Kafka Cluster. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "ksqldbcm/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ClusterList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


