# SqlV1beta1StatementList

`Statement` represents a core resource used to model SQL statements for execution. A statement generalizes DDL, DML, DQL, etc., but doesn’t attempt to handle session management or any higher-level functionality. The API allows you to list, create, read, and delete your statements. ## The Statements Model <SchemaDefinition schemaRef=\"#/components/schemas/sql.v1beta1.Statement\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | defaults to "sql/v1beta1"
**kind** | **str** | Kind defines the object this REST resource represents. | defaults to "StatementList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


