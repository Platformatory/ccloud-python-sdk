# NetworkingV1NetworkSpec

The desired state of the Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network | [optional] 
**cloud** | **str** | The cloud service provider in which the network exists. | [optional] 
**region** | **str** | The cloud service provider region in which the network exists. | [optional] 
**connection_types** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**cidr** | **bool, date, datetime, dict, float, int, list, str, none_type** | The IPv4 [CIDR block](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to used for this network. Must be &#x60;/16&#x60;. Required for VPC peering and AWS TransitGateway.  | [optional] 
**zones** | **[str]** | The 3 availability zones for this network. They can optionally be specified for AWS networks used with PrivateLink, for GCP networks used with Private Service Connect, and for AWS and GCP networks used with Peering. Otherwise, they are automatically chosen by Confluent Cloud.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  On Azure, zones are Confluent-chosen names (e.g. 1, 2, 3) since Azure does not  have universal zone identifiers.  | [optional] 
**zones_info** | **bool, date, datetime, dict, float, int, list, str, none_type** | Each item represents information related to a single zone.  Note - The attribute is in a [Limited Availability lifecycle stage](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)  | [optional] 
**dns_config** | **bool, date, datetime, dict, float, int, list, str, none_type** | DNS config only applies to PrivateLink network connection type.  When resolution is CHASED_PRIVATE, clusters in this network require both public and private DNS  to resolve cluster endpoints.  When resolution is PRIVATE, clusters in this network only require private DNS  to resolve cluster endpoints.  | [optional] 
**reserved_cidr** | **str** | The reserved CIDR config is used only by AWS networks with connection_types &#x3D; Vpc_Peering or Transit_Gateway  An IPv4 [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)   reserved for Confluent Cloud Network. Must be \\24.   If not specified, Confluent Cloud Network uses 172.20.255.0/24  Note - The attribute is in a [Limited Availability lifecycle stage](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)  | [optional] 
**environment** | **bool, date, datetime, dict, float, int, list, str, none_type** | The environment to which this belongs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


