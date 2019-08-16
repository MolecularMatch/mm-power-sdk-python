# Filter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | The term to search. | 
**root_term** | **str** | The root term corresponding to the term.  Terms can be synonyms of root term, whereas the root term is what is annotated the records being searched. | [optional] 
**facet** | **str** | The facet or domain the term belongs to.  provide PHRASE if unknown. | 
**filter_type** | **str** | Inclusion or exclusion search. | [optional] [default to 'include']
**distance_uom** | **str** | Used by DISTANCE filters only.  Specify distance in kilometers or miles. | [optional] [default to 'mi']
**postal_code** | **str** | Used by DISTANCE filters only.  Specify postal code to center distance search from. | [optional] 
**country_code** | **str** | Used by DISTANCE filters only.  Specify a 2 digit ISO-3166 country code to center distance search from. | [optional] 
**gene_expand** | **bool** | Used by MUTATION filters only.  If true, expand the search to include results maching the mutation gene. | [optional] 
**exclude_filter_only** | **bool** | To create a soft include filter, add excludeFilterOnly&#x3D;true (and specify filterType of include. | [optional] 
**error** | **str** |  | [optional] 
**ambiguous** | [**Filter**](Filter.md) |  | [optional] 



