# SearchResponseCT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_key** | **str** | Search key from a previous response to reconsititute a prior request. | [optional] 
**institution_id** | **str** | An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness. | [optional] 
**case_id** | **str** | For lab specific case tracking. | [optional] 
**total** | **int** | The total number of records that match this search. | 
**total_pages** | **int** | The number of results pages for this search based on the limit provided in the request. | 
**page** | **int** | The results page number this response corresponds to. | 
**rows** | [**list[ClinicalTrial]**](ClinicalTrial.md) | The array of results records.  Rows must be cast accordingly to ct, drug, publication, etc. | [optional] 
**rationalized** | [**list[Filter]**](Filter.md) | The array of filters and how they were interpreted by the MolecularMatch search engine. | [optional] 
**unrecognized** | [**list[Filter]**](Filter.md) | The array of filters that were not recognized by the MolecularMatch search engine. | [optional] 
**ambiguous_narrative** | **list[str]** | if true include a human readable ambiguous narrative.  This enables the consumer to activate \&quot;did you mean\&quot; search capability. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

