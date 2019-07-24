# Assertion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**external_id** | **list[str]** |  | [optional] 
**unique_key** | **str** |  | 
**hash_key** | **str** |  | 
**description** | **str** |  | [optional] 
**narrative** | **str** | A human readeable narrative describing the assertion. | [optional] 
**regulatory_body** | **str** | The regulatory body that has governance over this assertion. | 
**customer** | **str** | The customer identifier that has governance over this assertion. | 
**version** | **int** | The assertion set version number. | 
**regulatory_body_approved** | **bool** | If true, this assertion&#x27;s therapuetic context has regulatory approval. | [optional] 
**regulatory_body_approved_by** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**guideline_body** | **str** |  | [optional] 
**guideline_version** | **str** |  | [optional] 
**clinical_significance** | **str** |  | [optional] 
**biomarker_class** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**tags** | [**list[AssertionTags]**](AssertionTags.md) |  | [optional] 
**sources** | [**list[AssertionSources]**](AssertionSources.md) | The supporting evidence for this assertion. | [optional] 
**no_therapy_available** | **bool** | If true, there is no therapy related to this assertion. | [optional] 
**therapeutic_context** | [**list[AssertionTherapeuticContext]**](AssertionTherapeuticContext.md) | The therapies associated with this assertion. | [optional] 
**tiers** | [**list[AssertionTiers]**](AssertionTiers.md) |  | [optional] 
**released_tiers** | [**list[AssertionTiers]**](AssertionTiers.md) |  | [optional] 
**classifications** | [**list[AssertionClassifications]**](AssertionClassifications.md) |  | [optional] 
**prevalence** | [**list[AssertionPrevalence]**](AssertionPrevalence.md) |  | [optional] 



