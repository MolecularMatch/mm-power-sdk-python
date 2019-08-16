# ClinicalTrialLocationSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**us** | **bool** | Indicates if there are United States based locations. | [optional] 
**intl** | **bool** | Indicates if there are locations outside of the United States. | [optional] 
**count** | **float** | The number of trial sites. | [optional] 
**recruiting_count** | **float** | The number of trial sites that are recruiting patients. | [optional] 
**countries** | [**list[ClinicalTrialLocationSummaryCountries]**](ClinicalTrialLocationSummaryCountries.md) | Countries with locations offering this trial. | [optional] 
**nearest_distance** | **float** | The distance to the nearest trial location based on the distance unit of measure specified (miles if unspecified) from the search location (either geopoint, location object, or inferred search point bsaed on filters provided. | [optional] 
**nearest_location** | [**Facility**](Facility.md) |  | [optional] 



