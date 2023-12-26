# CdxV1RedeemTokenResponse

Share details for the consumer org or user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "RedeemTokenResponse"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**api_key** | **str** | The api key | [optional] [readonly] 
**secret** | **str** | The api key secret | [optional] [readonly] 
**kafka_bootstrap_url** | **str** | The kafka cluster bootstrap url | [optional] [readonly] 
**schema_registry_api_key** | **str** | The api key for schema registry | [optional] [readonly] 
**schema_registry_secret** | **str** | The api key secret for schema registry | [optional] [readonly] 
**schema_registry_url** | **str** | The schema registry endpoint url | [optional] [readonly] 
**resources** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | List of shared resources | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


