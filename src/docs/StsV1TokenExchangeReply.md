# StsV1TokenExchangeReply

token exchange response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | An JWT access token, issued by Confluent, in response to the token exchange request. Client application could use the access token to access confluent public api  | 
**issued_token_type** | **str** | The token type. Always matches the value of requested_token_type from the request. | 
**token_type** | **str** | Indicates the token type value. The only type that Confluent supports is Bearer | 
**expires_in** | **int** | The length of time, in seconds, that the access token is valid. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


