# IamV2IdentityProviderList

`IdentityProvider` objects represent external OAuth/OpenID Connect providers within Confluent Cloud.  The API allows you to list, create, read, update, and delete your Identity Provider.   Related guide: [OAuth for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).  ## The Identity Providers Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityProvider\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_providers_per_org` | Number of Identity Providers per organization | | `public_keys_per_provider` | Number of public keys saved per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "IdentityProviderList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


