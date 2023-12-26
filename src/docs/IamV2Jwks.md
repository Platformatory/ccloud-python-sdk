# IamV2Jwks

`JWKS` objects represent public key sets for a specific OAuth/OpenID Connect provider within Confluent Cloud.  The API allows you to refresh JWKS public key data.   Related guide: [OAuth for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).  ## The Jwks Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.Jwks\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "iam/v2"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "Jwks"
**spec** | [**IamV2JwksSpec**](IamV2JwksSpec.md) |  | [optional] 
**status** | [**IamV2JwksStatus**](IamV2JwksStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


