# ExporterUpdateRequest

Exporter update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Context type of the exporter. One of CUSTOM, NONE or AUTO (default) | [optional] 
**context** | **str** | Customized context of the exporter if contextType equals CUSTOM. | [optional] 
**subjects** | **[str]** | Name of each exporter subject | [optional] 
**subject_rename_format** | **str** | Format string for the subject name in the destination cluster, which may contain ${subject} as a placeholder for the originating subject name. For example, dc_${subject} for the subject orders will map to the destination subject name dc_orders. | [optional] 
**config** | **{str: (str,)}** | The map containing exporter’s configurations | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


