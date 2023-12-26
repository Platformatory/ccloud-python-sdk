# NetworkingV1NetworkStatus

The status of the Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecyle phase of the network:  PROVISIONING:  network provisioning is in progress;  READY:  network is ready;  FAILED: provisioning failed;  DEPROVISIONING: network deprovisioning is in progress;  | [readonly] 
**supported_connection_types** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**active_connection_types** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**error_code** | **str** | Error code if network is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if network is in a failed state | [optional] [readonly] 
**dns_domain** | **str** | The root DNS domain for the network if applicable. Present on networks that support PrivateLink. | [optional] [readonly] 
**zonal_subdomains** | **{str: (str,)}** | The DNS subdomain for each zone. Present on networks that support PrivateLink. Keys are zones and values are DNS domains.  | [optional] [readonly] 
**cloud** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The cloud-specific network details. These will be populated when the network reaches the READY state. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


