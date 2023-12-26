# IamV2IdentityPoolList

`IdentityPool` objects represent groups of identities tied to a given a `IdentityProvider` that authorizes them to Confluent Cloud resources.  It provides a mapping functionality of your `Identity Provider` user to a Confluent identity pool that is then used to provide access to Confluent Resources.   Related guide: [Use identity pools with your OAuth provider](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html).  ## The Identity Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityPool\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_pools_per_provider` | Number of Identity Pools per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] defaults to "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] defaults to "IdentityPoolList"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


