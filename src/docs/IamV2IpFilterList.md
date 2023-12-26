# IamV2IpFilterList

`IP Filter` objects are bindings between IP Groups and Confluent resource(s). For example, a binding between \"CorpNet\" and \"Management APIs\" will enforce that access must come from one of the CIDR blocks associated with CorpNet. If there are multiple IP filters bound to a resource, a request matching any of the CIDR blocks for any of the IP Group will allow the request. If there are no IP Filters for a resource, then access will be granted to requests originating from any IP Address.   ## The IP Filters Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IpFilter\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "IpFilterList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


