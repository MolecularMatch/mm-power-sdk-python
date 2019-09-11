# Drug

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | indicator of the quality of the match. | [optional] 
**mboost** | **float** | intrinsic boost to the record. | [optional] 
**id** | **str** | unique identifier. | [optional] 
**name** | **str** | The name of the drug. | [optional] 
**alias** | **str** | The most common name for the drug. | [optional] 
**description** | **str** | Descriptions of drug properties, treatments, history and regulatory status. | [optional] 
**composite** | **bool** | Indicates whether this drug is a composite of multiple drugs (combination therapy). | [optional] 
**approved** | **bool** | Indicates whether this drug has been approved by any regulating government. | [optional] 
**availability** | [**list[DrugAvailability]**](DrugAvailability.md) | Countries or jurisdictions where this drug is available. | [optional] 
**synonyms** | [**list[Synonym]**](Synonym.md) | Other names or identifiers that are associated with this drug. | [optional] 
**parents** | [**list[DrugParents]**](DrugParents.md) |  | [optional] 
**drugclass** | [**list[DrugDrugclass]**](DrugDrugclass.md) | The classes (pharmacological, treatment, chemical, etc.) of the drug inferred from the source or manually added. | [optional] 
**composite_tags** | [**list[DrugCompositeTags]**](DrugCompositeTags.md) | The individual drugs making up this composite drug | [optional] 
**brands** | [**list[DrugBrands]**](DrugBrands.md) | The manufacturer specific rendition of this drug. | [optional] 
**external_ids** | [**list[ExternalId]**](ExternalId.md) | Identifiers used in other websites or databases providing information about this drug. | [optional] 
**link** | **str** | DailyMed link for prescription label details. | [optional] 
**prices** | [**list[DrugPrices]**](DrugPrices.md) | Unit drug prices. | [optional] 
**dosages** | [**list[DrugDosages]**](DrugDosages.md) | A list of the commercially available dosages of the drug. | [optional] 
**pharmacology** | [**DrugPharmacology**](DrugPharmacology.md) |  | [optional] 
**molecular_alterations** | [**list[ConceptAssociation]**](ConceptAssociation.md) | Molecular concept associations established for this drug. | [optional] 
**contraindicated_alterations** | [**list[ConceptAssociation]**](ConceptAssociation.md) | Contraindicated Molecular concept associations established for this drug. | [optional] 
**assertions** | [**list[Assertion]**](Assertion.md) | Evidence in support of this drug. | [optional] 
**best_tier** | **str** | The highest tier evidence associated with this drug. | [optional] 
**met_tier** | **str** | The highest tier evidence associated with this drug where the criteria is fully met based on the search inputs. | [optional] 



