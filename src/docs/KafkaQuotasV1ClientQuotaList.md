# KafkaQuotasV1ClientQuotaList

`ClientQuota` objects represent Client Quotas you can set at the service account level.  The API allows you to list, create, read, update, and delete your client quotas.   Related guide: [Client Quotas in Confluent Cloud](https://docs.confluent.io/cloud/current/clusters/client-quotas.html).  ## The Client Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/kafka-quotas.v1.ClientQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "kafka-quotas/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "ClientQuotaList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


