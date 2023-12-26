# ConnectV1ConnectorExpansionInfo

Metadata of the connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connector. | [optional] 
**config** | **{str: (str,)}** | Configuration parameters for the connector. These configurations are the minimum set of key-value pairs (KVP) which are used to define how the connector connects Kafka to the external system. Some of these KVPs are common to all the connectors, such as connection parameters to Kafka, connector metadata, etc. The list of common connector configurations is as follows    - cloud.environment   - cloud.provider   - connector.class   - kafka.api.key   - kafka.api.secret   - kafka.endpoint   - kafka.region   - name  For example, a connector like &#x60;GcsSink&#x60; would have additional parameters such as &#x60;gcs.bucket.name&#x60;, &#x60;flush.size&#x60;, etc. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


