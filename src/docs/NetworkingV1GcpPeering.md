# NetworkingV1GcpPeering

GCP VPC Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The Google Cloud project ID associated with the VPC that you are peering with Confluent Cloud network.  | 
**vpc_network** | **str** | The name of the VPC that you are peering with Confluent Cloud network. | 
**kind** | **str** | Peering kind type. | defaults to "GcpPeering"
**import_custom_routes** | **bool** | Enable customer route import. For more information, see [Importing custom routes](https://cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes).  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


