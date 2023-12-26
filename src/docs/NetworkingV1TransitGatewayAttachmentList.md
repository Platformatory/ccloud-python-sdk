# NetworkingV1TransitGatewayAttachmentList

AWS Transit Gateway Attachments  Related guide: [APIs to manage AWS Transit Gateway Attachments](https://docs.confluent.io/cloud/current/networking/aws-transit-gateway.html).  ## The Transit Gateway Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.TransitGatewayAttachment\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `tgw_attachments_per_network` | Number of TGW attachments per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "TransitGatewayAttachmentList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


