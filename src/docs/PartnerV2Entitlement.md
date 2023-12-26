# PartnerV2Entitlement

`Entitlement` objects represent metadata about a marketplace entitlement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "partner/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Entitlement"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | [optional] 
**external_id** | **str** | The unique external ID of the entitlement (this should be unique to customer) | [optional] 
**name** | **str** | The name of the entitlement | [optional] 
**plan_id** | **str** | The plan ID the entitlement | [optional] 
**product_id** | **str** | The product ID of the entitlement | [optional] 
**usage_reporting_id** | **str** | The usage reporting ID of the entitlement (if usage reporting uses a different ID, otherwise, same as external_id)  | [optional] 
**resource_id** | **str** | The resource ID of the entitlement | [optional] 
**organization** | **bool, date, datetime, dict, float, int, list, str, none_type** | The organization associated with this object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


