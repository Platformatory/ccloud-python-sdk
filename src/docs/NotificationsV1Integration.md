# NotificationsV1Integration

You can create an `Integration` to specify how we can notify you when we receive an alert/notification for a subscription. Please note that you can only perform create, update and delete operations for integrations of type `Webhook`, `Slack` and `MsTeams`. You cannot create, update or delete integrations of type `RoleEmail` and `UserEmail`.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Integrations Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Integration\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `integrations_per_org` | Maximum number of integrations in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "notifications/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Integration"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**display_name** | **str** | A human readable name for the particular integration  | [optional] 
**description** | **str** | A human readable description for the particular integration  | [optional] 
**target** | **bool, date, datetime, dict, float, int, list, str, none_type** | Integration-specific details (integration targets)  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


