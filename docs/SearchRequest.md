# SearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_key** | **str** | Search key from a previous response to reconsititute a prior request. | [optional] 
**institution_id** | **str** | An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness. | [optional] 
**case_id** | **str** | For lab specific case tracking. | [optional] 
**start** | **int** | Starting record index for paging results. | [optional] 
**limit** | **int** | Number of records per page. | [optional] [default to 20]
**location_summary** | **bool** | If true, returns a summary location structure instead of the full array of trial locations. | [optional] 
**filter_narrative** | **bool** | If true, include a human readable filter narrative. | [optional] 
**fields** | **list[str]** | Provide a field list to customize the return records fields. | [optional] 
**filters** | [**list[Filter]**](Filter.md) |  | [optional] 
**geopoint** | [**SearchRequestGeopoint**](SearchRequestGeopoint.md) |  | [optional] 
**location** | [**SearchRequestLocation**](SearchRequestLocation.md) |  | [optional] 
**min_should_match** | [**SearchRequestMinShouldMatch**](SearchRequestMinShouldMatch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

