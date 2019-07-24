# DrugPharmacology

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indication** | **str** | The approved conditions, diseases, or states for which a drug can safely and effectively be used. An indication is considered to be FDA-approved when it has any of the following designations: NDA, ANDA, BLA, or OTC. May also include indications in other countries, such as Canada (through Health Canada) or in Europe (through the European Medicines Agency). | [optional] 
**pharmacodynamics** | **str** | A description of how the drug modifies or affects the organism it is being used in. May include effects in the body that are desired (enzyme or protein targets for example) and undesired (also known as “side effects”). This is in contrast to pharmacokinetics, which describes how the body modifies the drug being used. | [optional] 
**mechanism_of_action** | **str** | A component of pharmacodynamics that describes the biochemical interaction through which a drug produces its intended effect. May include the exact molecular protein or enzyme targets and/or a description of the physiological effects produced. | [optional] 
**absorption** | **str** | A description of the movement of the drug from the site of administration into the bloodstream or target tissue. Common pharmacokinetic metrics used to evaluate absorption include Area Under the Curve (AUC), bioavailability (F), maximum concentration (Cmax), and time to maximum concentration (Tmax). | [optional] 
**toxicity** | **str** | Any adverse reaction, or side effect, that may or may not occur with use of the drug. May be attributed to a number of effects including: an enhanced therapeutic effect, rare anaphylactic reactions, interactions with other medications, or unanticipated binding of the molecule at different sites within the body. | [optional] 
**protein_binding** | **str** | A description of the drug’s affinity for plama proteins and the proportion of the drug that is bound to them when in circulation within the body. | [optional] 
**metabolism** | **str** | A description of the chemical degradation of the drug molecule within the body; most commonly by enzymes from the Cytochrome P450 (CYP) system in the liver. | [optional] 
**half_life** | **str** | The period of time it takes for the amount of drug in the body to be reduced by one half. Provides a description of how quickly the drug is being eliminated and how much is available in the bloodstream. | [optional] 
**route_of_elimination** | **str** | A description of the pathway that is used to excrete the drug from the body. Common pharmacokinetic parameters used to evaluate excretion include elemination half life, renal clearance, and tracking of radiolabelled compounds through the renal and GI system. | [optional] 
**volume_of_distribution** | **str** | The Vd of a drug represents the degree to which it is distributed into body tissue compared to the plasma. | [optional] 
**clearance** | **str** | A pharmacokinetic measurement of the rate of removal of the drug from plasma, expressed as mL/min; reflects the rate of elimination of the drug. | [optional] 



