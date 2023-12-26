# NetworkingV1AwsTransitGatewayAttachment

AWS Transit Gateway Attachment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram_share_arn** | **str** | The full AWS Resource Name (ARN) for the AWS Resource Access Manager (RAM) Share of the Transit Gateways that you want Confluent Cloud to be attached to. | 
**transit_gateway_id** | **str** | The ID of the AWS Transit Gateway that you want Confluent CLoud to be attached to. | 
**routes** | [**[NetworkingV1Cidr]**](NetworkingV1Cidr.md) | List of destination routes. | 
**kind** | **str** | AWS Transit Gateway Attachment kind type. | defaults to "AwsTransitGatewayAttachment"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


