# SqlV1beta1StatementResultResults

A results property that contains a data property that contains an array of results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A data property that contains an array of results. Each entry in the array is a separate result.  The value of &#x60;op&#x60; attribute (if present) represents the kind of change that a row can describe in a changelog:  &#x60;0&#x60;: represents &#x60;INSERT&#x60; (&#x60;+I&#x60;), i.e. insertion operation;  &#x60;1&#x60;: represents &#x60;UPDATE_BEFORE&#x60; (&#x60;-U&#x60;), i.e. update operation with the previous content of the updated row. This kind should occur together with &#x60;UPDATE_AFTER&#x60; for modelling an update that needs to retract the previous row first. It is useful in cases of a non-idempotent update, i.e., an update of a row that is not  uniquely identifiable by a key;  &#x60;2&#x60;: represents &#x60;UPDATE_AFTER&#x60; (&#x60;+U&#x60;), i.e. update operation with new content of the updated row; This kind CAN occur together with &#x60;UPDATE_BEFORE&#x60; for modelling an update that needs to retract the previous row first or it describes an idempotent update, i.e., an update of a row that is uniquely identifiable by a key;  &#x60;3&#x60;: represents &#x60;DELETE&#x60; (&#x60;-D&#x60;), i.e. deletion operation;  Defaults to &#x60;0&#x60;.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


