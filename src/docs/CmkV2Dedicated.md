# CmkV2Dedicated

A dedicated cluster with its parameters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cku** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of Confluent Kafka Units (CKUs) for Dedicated cluster types. MULTI_ZONE dedicated clusters must have at least two CKUs.  | 
**kind** | **str** | Dedicated cluster type.  | defaults to "Dedicated"
**encryption_key** | **str** | The id of the encryption key that is used to encrypt the data in the Kafka cluster. (e.g. for Amazon Web Services, the Amazon Resource Name of the key).  | [optional] 
**zones** | **[str]** | The list of zones the cluster is in.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


