# SearchResponseDrug

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_key** | **str** | Search key from a previous response to reconsititute a prior request. | [optional] 
**institution_id** | **str** | An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness. | [optional] 
**case_id** | **str** | For lab specific case tracking. | [optional] 
**tiering_template** | **str** | The tiering template used to assess the quality of evidence. | 
**tiering_template_legend** | **object** | The tiering template legend explains the tiers pertaining to the template. | [optional] 
**total** | **int** | The total number of records that match this search. | 
**total_pages** | **int** | The number of results pages for this search based on the limit provided in the request. | 
**page** | **int** | The results page number this response corresponds to. | 
**rows** | [**list[Drug]**](Drug.md) | The array of drugs that match the search criteria. | [optional] 
**rationalized** | [**list[Filter]**](Filter.md) | The array of filters and how they were interpreted by the MolecularMatch search engine. | [optional] 
**unrecognized** | [**list[Filter]**](Filter.md) | The array of filters that were not recognized by the MolecularMatch search engine. | [optional] 
**filter_narrative** | **str** | A human readable narrative describing the search conducted. Can be used to provide \&quot;Showing results for\&quot; functionality. | [optional] 
**ambiguous_narrative** | **list[str]** | if true include a human readable ambiguous narrative.  This enables the consumer to activate \&quot;did you mean\&quot; search capability. | [optional] 



