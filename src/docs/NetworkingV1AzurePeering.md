# NetworkingV1AzurePeering

Azure VNet Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** | The Azure Tenant ID in which your Azure Subscription exists. Represents an organization in Azure Active Directory. You can find your Azure Tenant ID in the Azure Portal under [Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.  | 
**vnet** | **str** | The resource ID of the VNet that you are peering with Confluent Cloud. You can find the name of your Azure VNet in the [Azure Portal on the Overview tab of your Azure Virtual Network](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks). | 
**customer_region** | **str** | The region of the VNet you are peering with Confluent Cloud network. | 
**kind** | **str** | Peering kind type. | defaults to "AzurePeering"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


