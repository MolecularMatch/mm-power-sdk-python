# Oversight

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_dmc** | **bool** | Indication that a clinical study has a data monitoring committee. | [optional] 
**is_fda_regulated_drug** | **bool** | Indication that a clinical study is studying a drug product (including a biological product) subject to section 505 of the Federal Food, Drug, and Cosmetic Act or to section 351 of the Public Health Service Act. | [optional] 
**is_fda_regulated_device** | **bool** | Indication that a clinical study is studying a device product subject to section 510(k), 515, or 520(m) of the Federal Food, Drug, and Cosmetic Act. | [optional] 
**is_unapproved_device** | **bool** | Indication that at least one device product studied in the clinical study has not been previously approved or cleared by the U.S. Food and Drug Administration (FDA) for one or more uses. true: At least one studied FDA-regulated device product has not been previously approved or cleared by FDA.  false: All studied FDA-regulated device products have been previously approved or cleared by FDA. | [optional] 
**is_ppsd** | **bool** | Pediatric postmarket surveillance of a device. | [optional] 
**is_us_export** | **bool** | Whether any drug product (including a biological product) or device product studied in the clinical study is manufactured in the United States or one of its territories and exported for study in a clinical study in another country. Required if U.S. FDA-regulated Drug and/or U.S. FDA-regulated Device is true, U.S. FDA IND or IDE is false, and Facility Information does not include at least one U.S. location. | [optional] 



