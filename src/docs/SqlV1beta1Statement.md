# SqlV1beta1Statement

`Statement` represents a core resource used to model SQL statements for execution. A statement generalizes DDL, DML, DQL, etc., but doesn’t attempt to handle session management or any higher-level functionality. The API allows you to list, create, read, and delete your statements. ## The Statements Model <SchemaDefinition schemaRef=\"#/components/schemas/sql.v1beta1.Statement\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "sql/v1beta1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Statement"
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**name** | **str** | The user provided name of the resource, unique within this environment. | [optional] 
**organization_id** | **str** | The unique identifier for the organization. | [optional] 
**environment_id** | **str** | The unique identifier for the environment. | [optional] 
**spec** | [**SqlV1beta1StatementSpec**](SqlV1beta1StatementSpec.md) |  | [optional] 
**status** | [**SqlV1beta1StatementStatus**](SqlV1beta1StatementStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


