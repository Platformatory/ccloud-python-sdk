# NotificationsV1Subscription

`Subscription` objects represent the intent of the customers to get notifications of particular types. A subscription is created for a particular `NotificationType` and the user will get notifications on the `Integrations` that are provided while creating the subscription.  This API allows you to create, retrieve, and update subscriptions, as well as to view the list of all your subscriptions. You can also delete subscriptions with RECOMMENDED or OPTIONAL notification types. Subscriptions with REQUIRED notification types cannot be deleted.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Subscriptions Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Subscription\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "notifications/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Subscription"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**current_state** | **str** | Denotes the state of the subscription. When the subscription is ENABLED, the user will receive notification on the configured Integrations. If the subscription is DISABLED, the user will not recieve any notification for the configured notification type. Note that, you cannot disable a subscription for &#x60;REQUIRED&#x60; notification type.  | [optional] 
**notification_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of notification to subscribe to. | [optional] 
**integrations** | [**[GlobalObjectReference]**](GlobalObjectReference.md) | Integrations to which notifications are to be sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


