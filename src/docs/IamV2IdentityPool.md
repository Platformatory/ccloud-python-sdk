# IamV2IdentityPool

`IdentityPool` objects represent groups of identities tied to a given a `IdentityProvider` that authorizes them to Confluent Cloud resources.  It provides a mapping functionality of your `Identity Provider` user to a Confluent identity pool that is then used to provide access to Confluent Resources.   Related guide: [Use identity pools with your OAuth provider](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html).  ## The Identity Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityPool\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_pools_per_provider` | Number of Identity Pools per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "IdentityPool"
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**display_name** | **str** | The name of the &#x60;IdentityPool&#x60;. | [optional] 
**description** | **str** | A description of how this &#x60;IdentityPool&#x60; is used | [optional] 
**identity_claim** | **str** | The JSON Web Token (JWT) claim to extract the authenticating identity to Confluent resources from (see [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) for more details). This appears in the audit log records, showing, for example, that \&quot;identity Z used identity pool X to access topic A\&quot;. | [optional] 
**filter** | **str** | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#supported-common-expression-language-cel-filters) that specifies which identities can authenticate using your identity pool (see [Set identity pool filters](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#set-identity-pool-filters) for more details). | [optional] 
**principal** | **str** | Represents the federated identity associated with this pool. | [optional] [readonly] 
**state** | **str** | The current state of the identity pool | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


