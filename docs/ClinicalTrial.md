# ClinicalTrial

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | indicator of the quality of the match. | [optional] 
**mboost** | **float** | intrinsic boost to the record. | [optional] 
**import_date** | **datetime** | date this record was imported into the MolecularMatch database. | [optional] 
**id** | **str** | unique identifier. | 
**source** | **str** | native data source of this record | 
**brief_title** | **str** | A short title of the clinical study written in language intended for the lay public. The title should include, where possible, information on the participants, condition being evaluated, and intervention(s) studied. | [optional] 
**patient_title** | **str** | Patient friendly title for the clinical trial. | [optional] 
**title** | **str** | Official title for the clinical trial. | [optional] 
**brief_summary** | **str** | A short description of the clinical study, including a brief statement of the clinical study&#x27;s hypothesis, written in language intended for the lay public. | [optional] 
**brief_summary_preserved** | **str** | Formatted rendition of the briefSummary. | [optional] 
**summary** | **str** | Extended description of the protocol, including more technical information (as compared to the Brief Summary), if desired. Do not include the entire protocol; do not duplicate information recorded in other data elements, such as Eligibility Criteria or outcome measures. | [optional] 
**summary_preserved** | **str** | Formatted rendition of the summary. | [optional] 
**status** | **str** | Trial recruiting status. | [optional] 
**phase** | **str** | For a clinical trial of a drug product (including a biological product), the numerical phase of such clinical trial, consistent with terminology in 21 CFR 312.21 and in 21 CFR 312.85 for phase 4 studies. | [optional] [default to 'N/A']
**study_type** | **str** | The nature of the investigation or investigational use for which clinical study information is being submitted. | [optional] 
**study_design** | [**StudyDesign**](StudyDesign.md) |  | [optional] 
**start_date** | **datetime** | The estimated date on which the clinical study will be open for recruitment of participants, or the actual date on which the first participant was enrolled. | [optional] 
**completion_date** | **datetime** | The date the final participant was examined or received an intervention for purposes of final collection of data for the primary and secondary outcome measures and adverse events (for example, last participant’s last visit), whether the clinical study concluded according to the pre-specified protocol or was terminated | [optional] 
**first_received_date** | **datetime** | The date on which the study sponsor or investigator first submitted a study record to the trial registry (see source field). | [optional] 
**last_changed_date** | **datetime** | The most recent date that any information was updated for this trial. | [optional] 
**verification_date** | **datetime** | The date on which the responsible party last verified the clinical study information in the entire ClinicalTrials.gov record for the clinical study, even if no additional or updated information is being submitted. | [optional] 
**sponsors** | [**list[ClinicalTrialSponsors]**](ClinicalTrialSponsors.md) | The list of organizations or persons who initiated the study and who have authority and control over the study. | [optional] 
**conditions** | **list[str]** | Diseases/Conditions related to this trial. | [optional] 
**interventions** | [**list[Intervention]**](Intervention.md) | Specifies the intervention(s) associated with each arm or group. | [optional] 
**keywords** | **list[str]** | Words or phrases that best describe the protocol. Keywords help users find studies in the database. Use NLM&#x27;s Medical Subject Heading (MeSH)-controlled vocabulary terms where appropriate. Be as specific and precise as possible. | [optional] 
**arm_groups** | [**list[ArmGroup]**](ArmGroup.md) | Pre-specified groups of participants in a clinical trial assigned to receive specific interventions (or no intervention) according to a protocol. | [optional] 
**primary_outcomes** | [**list[Outcome]**](Outcome.md) | The outcome that an investigator considers to be the most important among the many outcomes that are to be examined in the study. | [optional] 
**secondary_outcomes** | [**list[Outcome]**](Outcome.md) |  | [optional] 
**other_outcomes** | [**list[Outcome]**](Outcome.md) |  | [optional] 
**eligibility** | [**Eligibility**](Eligibility.md) |  | [optional] 
**enrollment** | **int** | The estimated total number of participants to be enrolled (target number) or the actual total number of participants that are enrolled in the clinical study. | [optional] 
**min_age** | **float** | The numerical value, if any, for the minimum age a potential participant must meet to be eligible for the clinical study. | 
**max_age** | **float** | The numerical value, if any, for the maximum age a potential participant can be to be eligible for the clinical study. | 
**gender** | **list[str]** | The sex and, if applicable, gender of the participants eligible to participate in the clinical study. | [optional] 
**overall_official** | [**list[Contact]**](Contact.md) | Person responsible for the overall scientific leadership of the protocol, including study principal investigator. | [optional] 
**overall_contact** | [**Contact**](Contact.md) |  | [optional] 
**overall_contact_backup** | [**Contact**](Contact.md) |  | [optional] 
**location_summary** | [**ClinicalTrialLocationSummary**](ClinicalTrialLocationSummary.md) |  | [optional] 
**locations** | [**list[Facility]**](Facility.md) | Information about the sites offering this trial. | [optional] 
**countries** | [**list[ClinicalTrialCountries]**](ClinicalTrialCountries.md) | Countries with sites offering this trial. | [optional] 
**inclusion_criteria** | **str** | A limited list of criteria for selection of participants in the clinical study, provided in terms of inclusion criteria and suitable for assisting potential participants in identifying clinical studies of interest. | [optional] 
**inclusion_criteria_preserved** | **str** | Formatted rendition of the inclusionCriteria. | [optional] 
**exclusion_criteria** | **str** | A limited list of criteria for selection of participants in the clinical study, provided in terms of exclusion criteria and suitable for assisting potential participants in identifying clinical studies of interest. | [optional] 
**exclusion_criteria_preserved** | **str** | Formatted rendition of the exclusionCriteria. | [optional] 
**synonyms** | [**list[Synonym]**](Synonym.md) | Any identifier other than the organization&#x27;s Unique Protocol Identification Number or the NCT number that is assigned to the clinical study. | [optional] 
**acronym** | **str** | An acronym or abbreviation used publicly to identify the clinical study. | [optional] 
**link** | **str** | URL to registry listing of this trial. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Concept associations established for this trial. | [optional] 
**molecular_alterations** | [**list[ConceptAssociation]**](ConceptAssociation.md) | Molecular concept associations established for this trial. | [optional] 
**stats** | **object** |  | [optional] 



