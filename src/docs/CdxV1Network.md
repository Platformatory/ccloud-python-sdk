# CdxV1Network

The shared cluster's network configurations for consumer to setup private link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "cdx/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Network"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**kafka_bootstrap_url** | **str** | The kafka cluster bootstrap url | [optional] [readonly] 
**zones** | **[str]** | The 3 availability zones for this network. They can optionally be specified for AWS networks used with PrivateLink. Otherwise, they are automatically chosen by Confluent Cloud.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  On Azure, zones are Confluent-chosen names (e.g. 1, 2, 3) since Azure does not  have universal zone identifiers.  | [optional] 
**dns_domain** | **str** | The root DNS domain for the network if applicable. | [optional] [readonly] 
**zonal_subdomains** | **{str: (str,)}** | The DNS subdomain for each zone. Present on networks that support PrivateLink. Keys are zones and values are DNS domains.  | [optional] [readonly] 
**cloud** | **bool, date, datetime, dict, float, int, list, str, none_type** | The cloud-specific network details. These will be populated when the network reaches the READY state. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


