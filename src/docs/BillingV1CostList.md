# BillingV1CostList

`Cost` objects represent the aggregated billing costs for an organization   Related guide: [Retrieve costs for a range of dates](https://docs.confluent.io/cloud/current/billing/overview.html#retrieve-costs-for-a-range-of-dates).  ## The Costs Model <SchemaDefinition schemaRef=\"#/components/schemas/billing.v1.Cost\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "billing/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "CostList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


