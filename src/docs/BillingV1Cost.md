# BillingV1Cost

`Cost` objects represent the aggregated billing costs for an organization   Related guide: [Retrieve costs for a range of dates](https://docs.confluent.io/cloud/current/billing/overview.html#retrieve-costs-for-a-range-of-dates).  ## The Costs Model <SchemaDefinition schemaRef=\"#/components/schemas/billing.v1.Cost\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "billing/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Cost"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**start_date** | **date** | Start date of time period (inclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | [optional] 
**end_date** | **date** | End date of time period (exclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | [optional] 
**granularity** | **str** | Granularity at which each line item is aggregated. | [optional]  if omitted the server will use the default value of "DAILY"
**network_access_type** | **str** | Network access type for the cluster. | [optional] 
**product** | **str** | Product name. | [optional] 
**line_type** | **str** | Type of the line item. | [optional] 
**price** | **float** | Price for the line item in dollars. | [optional] 
**unit** | **str** | Unit of the line item. | [optional] 
**quantity** | **float** | Quantity of the line item. | [optional] 
**original_amount** | **float** | Original amount accrued for this line item. | [optional] 
**discount_amount** | **float** | Amount discounted from the original amount in dollars. | [optional] 
**amount** | **float** | Final amount after deducting discounts. | [optional] 
**resource** | **bool, date, datetime, dict, float, int, list, str, none_type** | The resource for a given object | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


