# Drug

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mboost** | **float** | intrinsic boost to the record. | [optional] 
**id** | **str** | unique identifier. | 
**name** | **str** | The name of the drug. | 
**alias** | **str** | The most common name for the drug. | [optional] 
**description** | **str** | Descriptions of drug chemical properties, history and regulatory status. | [optional] 
**composite** | **bool** |  | [optional] 
**approved** | **bool** | Indicates whether this drug has been approved by any regulating government. | 
**availability** | [**list[DrugAvailability]**](DrugAvailability.md) | Countries or jurisdictions where this drug is available. | [optional] 
**synonyms** | [**list[DrugSynonyms]**](DrugSynonyms.md) | Other names or identifiers that are associated with this drug. | [optional] 
**parents** | [**list[DrugParents]**](DrugParents.md) |  | [optional] 
**drugclass** | [**list[DrugDrugclass]**](DrugDrugclass.md) |  | [optional] 
**composite_tags** | [**list[DrugCompositeTags]**](DrugCompositeTags.md) |  | [optional] 
**brands** | [**list[DrugBrands]**](DrugBrands.md) |  | [optional] 
**indication_text** | **str** |  | [optional] 
**contraindication_text** | **str** |  | [optional] 
**mechanism_text** | **str** |  | [optional] 
**rxcui** | **list[str]** |  | [optional] 
**external_ids** | [**list[DrugExternalIds]**](DrugExternalIds.md) | Identifiers used in other websites or databases providing information about this drug. | [optional] 
**link** | **str** |  | [optional] 
**prices** | [**list[DrugPrices]**](DrugPrices.md) | Unit drug prices. | [optional] 
**dosages** | [**list[DrugDosages]**](DrugDosages.md) | A list of the commercially available dosages of the drug. | [optional] 
**pharmacology** | [**DrugPharmacology**](DrugPharmacology.md) |  | [optional] 
**phase_and_trials_score** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

