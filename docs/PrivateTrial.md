# PrivateTrial

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique study identifier. | [optional] 
**institution_id** | **str** | Unique institution identifier. | 
**institution_study_id** | **str** | Unique study identifier (for the institution). | 
**registry_id** | **str** | The public registry study id.  This is only populated once the trial is no longer a private trial. | [optional] 
**visible_to_idn** | **bool** | If true, then this trial will be visible to the entire IDN, else it is visible only to the owning institution. | [optional] [default to True]
**brief_title** | **str** | A short title of the clinical study written in language intended for the lay public. The title should include, where possible, information on the participants, condition being evaluated, and intervention(s) studied. | [optional] 
**acronym** | **list[str]** | Acronyms or abbreviations used publicly to identify the clinical study. | [optional] 
**official_title** | **str** | Official title for the clinical trial. | 
**sponsors** | [**list[ClinicalTrialSponsors]**](ClinicalTrialSponsors.md) | The list of organizations or persons who initiated the study and who have authority and control over the study. | [optional] 
**source** | **str** | Native data source of this record | [optional] 
**oversight** | [**Oversight**](Oversight.md) |  | [optional] 
**brief_summary** | **str** | A short description of the clinical study, including a brief statement of the clinical study&#x27;s hypothesis, written in language intended for the lay public. | [optional] 
**detailed_description** | **str** | Extended description of the protocol, including more technical information (as compared to the Brief Summary), if desired. Do not include the entire protocol; do not duplicate information recorded in other data elements, such as Eligibility Criteria or outcome measures. | [optional] 
**status** | **str** | Trial recruiting status. | 
**start_date** | **datetime** | The estimated date on which the clinical study will be open for recruitment of participants, or the actual date on which the first participant was enrolled. | 
**completion_date** | **datetime** | The date the final participant was examined or received an intervention for purposes of final collection of data for the primary and secondary outcome measures and adverse events (for example, last participant’s last visit), whether the clinical study concluded according to the pre-specified protocol or was terminated | [optional] 
**phase** | **str** | For a clinical trial of a drug product (including a biological product), the numerical phase of such clinical trial, consistent with terminology in 21 CFR 312.21 and in 21 CFR 312.85 for phase 4 studies. | [optional] [default to 'N/A']
**study_type** | **str** | The nature of the investigation or investigational use for which clinical study information is being submitted. | 
**has_expanded_access** | **bool** | Whether there is expanded access to the investigational product for patients who do not qualify for enrollment in a clinical trial. Expanded Access for investigational drug products (including biological products) includes all expanded access types under section 561 of the Federal Food, Drug, and Cosmetic Act: (1) for individual participants, including emergency use; (2) for intermediate-size participant populations; and (3) under a treatment IND or treatment protocol. | [optional] 
**expanded_access** | [**ExpandedAccess**](ExpandedAccess.md) |  | [optional] 
**study_design** | [**StudyDesign**](StudyDesign.md) |  | [optional] 
**primary_outcome** | [**list[Outcome]**](Outcome.md) | The outcome that an investigator considers to be the most important among the many outcomes that are to be examined in the study. | [optional] 
**secondary_outcome** | [**list[Outcome]**](Outcome.md) |  | [optional] 
**other_outcome** | [**list[Outcome]**](Outcome.md) |  | [optional] 
**number_of_arms** | **int** | The number of trial arms. | [optional] [default to 1]
**number_of_groups** | **int** | The number of trial groups. | [optional] [default to 1]
**enrollment** | **int** | The estimated total number of participants to be enrolled (target number) or the actual total number of participants that are enrolled in the clinical study. | [optional] 
**condition** | **list[str]** | Diseases/Conditions related to this trial. | [optional] 
**arm_group** | [**list[ArmGroup]**](ArmGroup.md) | Pre-specified groups of participants in a clinical trial assigned to receive specific interventions (or no intervention) according to a protocol. | [optional] 
**intervention** | [**list[Intervention]**](Intervention.md) | Specifies the intervention(s) associated with each arm or group. | [optional] 
**biospec_retention** | **str** |  | [optional] [default to 'None Retained']
**biospec_descr** | **str** |  | [optional] 
**eligibility** | [**Eligibility**](Eligibility.md) |  | [optional] 
**overall_official** | [**list[Investigator]**](Investigator.md) | Person responsible for the overall scientific leadership of the protocol, including study principal investigator. | [optional] 
**overall_contact** | [**Contact**](Contact.md) |  | [optional] 
**overall_contact_backup** | [**Contact**](Contact.md) |  | [optional] 
**location** | [**list[Location]**](Location.md) | Information about the locations offering this trial. | 
**location_countries** | **list[str]** | Countries with locations offering this trial. | [optional] 
**link** | **str** | URL to institution (if private) or registry listing of this trial. | [optional] 
**reference** | [**list[Reference]**](Reference.md) | Reference publications pertaining to this trial. | [optional] 
**verification_date** | **datetime** | The date on which the responsible party last verified the clinical study information in the entire ClinicalTrials.gov record for the clinical study, even if no additional or updated information is being submitted. | [optional] 
**study_first_submitted** | **datetime** | The date on which the study sponsor or investigator first submitted a study record to the trial registry. | [optional] 
**study_first_posted** | **datetime** | The date on which the study was first made public on trial registry. | [optional] 
**last_update_posted** | **datetime** | The most recent date that any information was updated for this trial. | [optional] 
**keyword** | **list[str]** | Words or phrases that best describe the protocol. Keywords help users find studies in the database. Use NLM&#x27;s Medical Subject Heading (MeSH)-controlled vocabulary terms where appropriate. Be as specific and precise as possible. | [optional] 
**responsible_party** | [**list[ResponsibleParty]**](ResponsibleParty.md) | The entities and individuals responsible for this trial. | [optional] 
**processing_status** | **str** | Indication of its level of readiness and incorporation into the MolecularMatch Knowledge base. | [optional] [default to 'received']
**test** | **bool** | A flag to mark test private trials. | [optional] 



