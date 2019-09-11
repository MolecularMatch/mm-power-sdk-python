# Assertion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | indicator of the quality of the match. | [optional] 
**id** | **str** |  | [optional] 
**external_id** | **list[str]** | Optional institution specific identifier. | [optional] 
**unique_key** | **str** | Unique identifer inclusive of version. | [optional] 
**hash_key** | **str** | Static identifier agnostic of version. | [optional] 
**description** | **str** | Detailed description of the assertion. | [optional] 
**narrative** | **str** | A human readeable narrative describing the assertion. | [optional] 
**regulatory_body** | **str** | The regulatory body that has governance over this assertion. | 
**customer** | **str** | The customer identifier that has governance over this assertion. | 
**version** | **int** | The assertion set version number. | 
**regulatory_body_approved** | **bool** | If true, this assertion&#x27;s therapuetic context has regulatory approval. | [optional] 
**regulatory_body_approved_by** | **str** | Governing body granting approval. | [optional] 
**direction** | **str** | Indicates whether assertion supports or does not support the therapy. | [optional] 
**guideline_body** | **str** | A professional committee recommendation. | [optional] 
**guideline_version** | **str** | Release version of professional committee recommendation. | [optional] 
**clinical_significance** | **str** | Utility of biomarker in clinical setting. | [optional] 
**biomarker_class** | **str** | Indicator of response to therapy | [optional] 
**expression** | **str** | mathematical expression characterizing the clinical scope of the assertion. | [optional] 
**sources** | [**list[AssertionSources]**](AssertionSources.md) | The supporting evidence for this assertion. | [optional] 
**no_therapy_available** | **bool** | If true, there is no therapy related to this assertion. | [optional] 
**therapeutic_context** | [**list[AssertionTherapeuticContext]**](AssertionTherapeuticContext.md) | The therapies associated with this assertion. | [optional] 
**tier** | **str** | The tiering template specific tier associated with the therapy. | [optional] 
**tier_explanation** | [**list[TierExplanation]**](TierExplanation.md) | The explanation of how the tier was calculated. | [optional] 
**criteria_unmet** | [**list[ConceptAssociation]**](ConceptAssociation.md) |  | [optional] 
**criteria_met** | [**list[ConceptAssociation]**](ConceptAssociation.md) |  | [optional] 
**classifications** | [**list[AssertionClassifications]**](AssertionClassifications.md) |  | [optional] 
**prevalence** | [**list[AssertionPrevalence]**](AssertionPrevalence.md) |  | [optional] 
**variant_info** | [**list[VariantInfo]**](VariantInfo.md) | Genomic information pertaining to variant. | [optional] 



