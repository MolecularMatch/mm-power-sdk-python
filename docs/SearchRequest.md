# SearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_key** | **str** | Search key from a previous response to reconsititute a prior request. | [optional] 
**institution_id** | **str** | An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness. | [optional] 
**case_id** | **str** | For lab specific case tracking. | [optional] 
**tiering_template** | **str** | Applies to drug and assertion search.  Optionally supply the tiering template. | [optional] 
**start** | **int** | Starting record index for paging results. | [optional] 
**limit** | **int** | Number of records per page. | [optional] [default to 20]
**fields** | **list[str]** | Provide a field list to customize the return records fields. | [optional] 
**filters** | [**list[Filter]**](Filter.md) |  | [optional] 
**geopoint** | [**SearchRequestGeopoint**](SearchRequestGeopoint.md) |  | [optional] 
**location** | [**SearchRequestLocation**](SearchRequestLocation.md) |  | [optional] 
**min_should_match** | [**SearchRequestMinShouldMatch**](SearchRequestMinShouldMatch.md) |  | [optional] 



