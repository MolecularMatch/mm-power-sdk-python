# MongoTrial

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mboost** | **float** | intrinsic boost to the record. | [optional] 
**import_date** | **datetime** | date this record was imported into the MolecularMatch database. | [optional] 
**id** | **str** | unique identifier. | 
**source** | **str** | native data source of this record | 
**exclude** | **bool** | soft exclude from the MolecularMatch dataset. | [optional] 
**custom** | **bool** | custom record in the MolecularMatch dataset | [optional] 
**brief_title** | **str** | Abbreviated title for the clinical trial. | [optional] 
**patient_title** | **str** | Patient friendly title for the clinical trial. | [optional] 
**title** | **str** | Official title for the clinical trial. | [optional] 
**brief_summary** | **str** | Abbreviated summary for the clinical trial. | [optional] 
**summary** | **str** | Official title for the clinical trial. | [optional] 
**status** | **str** |  | [optional] 
**phase** | **str** | Recruitment status for the clinical trial. | [optional] 
**study_type** | **str** |  | [optional] 
**study_design** | [**MongoTrialStudyDesign**](MongoTrialStudyDesign.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**completion_date** | **datetime** |  | [optional] 
**first_received_date** | **datetime** |  | [optional] 
**last_changed_date** | **datetime** |  | [optional] 
**verification_date** | **datetime** |  | [optional] 
**sponsors** | [**list[ClinicalTrialSponsors]**](ClinicalTrialSponsors.md) |  | [optional] 
**conditions** | **list[str]** |  | [optional] 
**interventions** | [**list[ClinicalTrialInterventions]**](ClinicalTrialInterventions.md) |  | [optional] 
**keywords** | **list[str]** |  | [optional] 
**arm_groups** | [**list[ClinicalTrialArmGroups]**](ClinicalTrialArmGroups.md) |  | [optional] 
**primary_outcomes** | [**list[ClinicalTrialPrimaryOutcomes]**](ClinicalTrialPrimaryOutcomes.md) |  | [optional] 
**secondary_outcomes** | [**list[ClinicalTrialPrimaryOutcomes]**](ClinicalTrialPrimaryOutcomes.md) |  | [optional] 
**other_outcomes** | [**list[ClinicalTrialPrimaryOutcomes]**](ClinicalTrialPrimaryOutcomes.md) |  | [optional] 
**eligibility** | [**ClinicalTrialEligibility**](ClinicalTrialEligibility.md) |  | [optional] 
**enrollment** | **int** |  | [optional] 
**min_age** | **float** |  | 
**max_age** | **float** |  | 
**gender** | **list[str]** |  | [optional] 
**overall_official** | [**list[ClinicalTrialOverallOfficial]**](ClinicalTrialOverallOfficial.md) |  | [optional] 
**overall_contact** | [**ClinicalTrialOverallOfficial**](ClinicalTrialOverallOfficial.md) |  | [optional] 
**overall_contact_backup** | [**ClinicalTrialOverallOfficial**](ClinicalTrialOverallOfficial.md) |  | [optional] 
**mm_email** | **str** |  | [optional] 
**wrong_email** | **bool** |  | [optional] 
**locations** | [**list[MongoTrialLocations]**](MongoTrialLocations.md) |  | [optional] 
**countries** | [**list[ClinicalTrialCountries]**](ClinicalTrialCountries.md) |  | [optional] 
**inclusion_criteria** | **str** |  | [optional] 
**exclusion_criteria** | **str** |  | [optional] 
**synonyms** | [**list[MongoTrialSynonyms]**](MongoTrialSynonyms.md) |  | [optional] 
**acronym** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**who_link** | **str** |  | [optional] 
**valid** | [**Object**](Object.md) |  | [optional] 
**valid_message** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

