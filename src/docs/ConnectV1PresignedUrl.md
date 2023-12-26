# ConnectV1PresignedUrl

Request a presigned upload URL for new Custom Connector Plugin. Note that the URL policy expires in one hour. If the policy expires, you can request a new presigned upload URL.  Related guide: [Custom Connector Plugin API](https://docs.confluent.io/cloud/current/connectors/connect-api-section.html).   ## The Presigned Urls Model <SchemaDefinition schemaRef=\"#/components/schemas/connect.v1.PresignedUrl\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly]  if omitted the server will use the default value of "connect/v1"
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly]  if omitted the server will use the default value of "PresignedUrl"
**content_format** | **str** | Content format of the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_id** | **str** | Unique identifier of this upload. | [optional] [readonly] 
**upload_url** | **str** | Upload URL for the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_form_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Upload form data of the Custom Connector Plugin. All values should be strings. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


