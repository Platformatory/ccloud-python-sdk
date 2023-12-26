# SrcmV3ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The cluster name. | [optional] [readonly] 
**package** | **str** | The billing package.  Note: Clusters can be upgraded from ESSENTIALS to ADVANCED, but cannot be downgraded from ADVANCED to ESSENTIALS.  | [optional] 
**http_endpoint** | **str** | The cluster HTTP request URL. | [optional] [readonly] 
**cloud** | **str** | The cloud service provider in which the cluster is running. | [optional] 
**region** | **str** | The cloud service provider region where the cluster is running. | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


