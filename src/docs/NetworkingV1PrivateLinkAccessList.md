# NetworkingV1PrivateLinkAccessList

Add or remove access to PrivateLink endpoints by AWS account, Azure subscription and GCP project ID.  Related guide: [Private Links Overview](https://docs.confluent.io/cloud/current/networking/private-links/index.html).  ## The Private Link Accesses Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAccess\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `private_link_accounts_per_network` | Number of AWS accounts per network | | `private_link_subscriptions_per_network` | Number of Azure subscriptions per network | | `private_service_connect_projects_per_network` | Number of GCP projects per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "networking/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "PrivateLinkAccessList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


