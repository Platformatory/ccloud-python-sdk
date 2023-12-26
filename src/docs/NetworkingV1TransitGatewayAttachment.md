# NetworkingV1TransitGatewayAttachment

AWS Transit Gateway Attachments  Related guide: [APIs to manage AWS Transit Gateway Attachments](https://docs.confluent.io/cloud/current/networking/aws-transit-gateway.html).  ## The Transit Gateway Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.TransitGatewayAttachment\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `tgw_attachments_per_network` | Number of TGW attachments per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "TransitGatewayAttachment"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**spec** | [**NetworkingV1TransitGatewayAttachmentSpec**](NetworkingV1TransitGatewayAttachmentSpec.md) |  | [optional] 
**status** | [**NetworkingV1TransitGatewayAttachmentStatus**](NetworkingV1TransitGatewayAttachmentStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


