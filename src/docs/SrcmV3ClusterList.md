# SrcmV3ClusterList

`Clusters` objects represent Schema Registry Clusters on Confluent Cloud.  The API allows you to list and read your Schema Registry clusters.   Related guide: [Confluent Cloud Schema Registry Cluster APIs](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-cluster-management).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v3.Cluster\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "srcm/v3"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ClusterList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


