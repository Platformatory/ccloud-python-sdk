# NetworkingV1AwsPeering

AWS VPC Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **bool, date, datetime, dict, float, int, list, str, none_type** | The AWS account ID associated with the VPC you are peering with Confluent Cloud network. | 
**vpc** | **str** | The VPC ID you are peering with Confluent Cloud network. | 
**routes** | [**[NetworkingV1Cidr]**](NetworkingV1Cidr.md) | The [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) of the VPC you are peering with Confluent Cloud network. This is used by Confluent Cloud network to route traffic back to your network. The CIDR block must be a private range and cannot overlap with the Confluent Cloud CIDR block.  | 
**customer_region** | **str** | The region of the VPC you are peering with Confluent Cloud network. | 
**kind** | **str** | Peering kind type. | defaults to "AwsPeering"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


