# ObjectMeta

ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | **str** | Self is a Uniform Resource Locator (URL) at which an object can be addressed. This URL encodes the service location, API version, and other particulars necessary to locate the resource at a point in time | [readonly] 
**resource_name** | **str** | Resource Name is a Uniform Resource Identifier (URI) that is globally unique across space and time. It is represented as a Confluent Resource Name | [optional] [readonly] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


