# NetworkingV1IpAddress

IP Addresses  Related guide: [Use Public Egress IP addresses on Confluent Cloud](https://docs.confluent.io/cloud/current/networking/static-egress-ip-addresses.html)  ## The IP Addresses Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.IpAddress\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "IpAddress"
**ip_prefix** | **str** | The IP Address range. | [optional] 
**cloud** | **str** | The cloud service provider in which the address exists. | [optional] 
**region** | **str** | The region/location where the IP Address is in use. | [optional] 
**services** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**address_type** | **str** | Whether the address is used for egress or ingress. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


