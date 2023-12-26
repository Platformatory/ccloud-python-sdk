# IamV2RoleBinding

A role binding grants a Principal a role on resources that match a pattern.  The API allows you to perform create, delete, and list operations on role bindings.   Related guide: [Role-Based Access Control (RBAC)](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html).  ## The Role Bindings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.RoleBinding\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "RoleBinding"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**principal** | **str** | The principal User or Group to bind the role to | [optional] 
**role_name** | **str** | The name of the role to bind to the principal | [optional] 
**crn_pattern** | **str** | A CRN that specifies the scope and resource patterns necessary for the role to bind | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


