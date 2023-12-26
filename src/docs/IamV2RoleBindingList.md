# IamV2RoleBindingList

A role binding grants a Principal a role on resources that match a pattern.  The API allows you to perform create, delete, and list operations on role bindings.   Related guide: [Role-Based Access Control (RBAC)](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html).  ## The Role Bindings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.RoleBinding\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "RoleBindingList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


