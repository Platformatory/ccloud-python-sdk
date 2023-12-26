# NotificationsV1IntegrationList

You can create an `Integration` to specify how we can notify you when we receive an alert/notification for a subscription. Please note that you can only perform create, update and delete operations for integrations of type `Webhook`, `Slack` and `MsTeams`. You cannot create, update or delete integrations of type `RoleEmail` and `UserEmail`.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Integrations Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Integration\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `integrations_per_org` | Maximum number of integrations in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "notifications/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "IntegrationList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


