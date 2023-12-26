# CreateLinkRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_cluster_id** | **str** |  | [optional] 
**destination_cluster_id** | **str** |  | [optional] 
**remote_cluster_id** | **str** | The expected remote cluster ID. | [optional] 
**cluster_link_id** | **str** | The expected cluster link ID. Can be provided when creating the second side of a bidirectional link for validating the link ID is as expected. If it&#39;s not provided, it&#39;s inferred from the remote cluster. | [optional] 
**configs** | [**[ConfigData]**](ConfigData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


