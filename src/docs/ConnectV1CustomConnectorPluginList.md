# ConnectV1CustomConnectorPluginList

CustomConnectorPlugins objects represent Custom Connector Plugins on Confluent Cloud. The API allows you to list, create, read, update, and delete your Custom Connector Plugins. Related guide: [Custom Connector Plugin API](https://docs.confluent.io/cloud/current/connectors/connect-api-section.html).   ## The Custom Connector Plugins Model <SchemaDefinition schemaRef=\"#/components/schemas/connect.v1.CustomConnectorPlugin\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "connect/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "CustomConnectorPluginList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


