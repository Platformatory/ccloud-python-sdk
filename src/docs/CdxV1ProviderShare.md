# CdxV1ProviderShare

`ProviderShare` object respresents the share that you have created through Stream Sharing.   Related guide: [Provider Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/produce-shared-data.html#stream-shares).  ## The Provider Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "ProviderShare"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**consumer_user_name** | **str** | Name of the consumer | [optional] [readonly] 
**consumer_organization_name** | **str** | Consumer organization name | [optional] [readonly] 
**provider_user_name** | **str** | Name or email of the provider user. Deprecated | [optional] [readonly] 
**delivery_method** | **str** | Method by which the invite will be delivered | [optional] 
**consumer_restriction** | **bool, date, datetime, dict, float, int, list, str, none_type** | Restrictions on the consumer that can redeem this token | [optional] 
**invited_at** | **datetime** | The date and time at which consumer was invited | [optional] [readonly] 
**invite_expires_at** | **datetime** | The date and time at which the invitation will expire. Only for invited shares | [optional] [readonly] 
**redeemed_at** | **datetime** | The date and time at which the invite was redeemed | [optional] [readonly] 
**provider_user** | **bool, date, datetime, dict, float, int, list, str, none_type** | The provider user/inviter | [optional] [readonly] 
**service_account** | **bool, date, datetime, dict, float, int, list, str, none_type** | The service account associated with this object. | [optional] 
**cloud_cluster** | **bool, date, datetime, dict, float, int, list, str, none_type** | The cloud cluster to which this belongs. | [optional] 
**status** | [**CdxV1ProviderShareStatus**](CdxV1ProviderShareStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


