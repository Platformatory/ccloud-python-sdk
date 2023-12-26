# IamV2JwksObject

`JWKS` contains the published keys for the given OpenIDProvider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Specifies the cryptographic algorithm family used with the key | 
**kid** | **str** | Specifies the key-id issued by the OpenIDProvider for the particular tenant | 
**alg** | **str** | Specifies the algorithm to be used to generate the public key | 
**use** | **str** | Specifies the intended usage of the key | [optional] 
**n** | **str** | Specifies the modulus of the RSA public key. Represented as a Base64urlUInt-encoded value | [optional] 
**e** | **str** | Specifies the exponent of the RSA public key. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


