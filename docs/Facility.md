# Facility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**street** | **str** | Site street name. | [optional] 
**number** | **str** | Site street number. | [optional] 
**country** | **str** | Site country. | [optional] 
**name** | **str** | Site name. | [optional] 
**po_box** | **str** | Site P.O. Box. | [optional] 
**city** | **str** | Site city. | [optional] 
**state** | **str** | Site state or sub division. | [optional] 
**zip** | **str** | Site postal code. | [optional] 
**lat** | **float** | Latitude | [optional] 
**lon** | **float** | Longitude | [optional] 
**geo** | [**FacilityGeo**](FacilityGeo.md) |  | [optional] 
**status** | **str** | Site specific recruiting status. | [optional] 
**link** | **str** | Country (competent authority) specific link (available for EU trials only) | [optional] 
**first_name** | **str** | Site primary contact first name. | [optional] 
**middle_name** | **str** | Site primary contact middle name. | [optional] 
**last_name** | **str** | Site primary contact last name. | [optional] 
**degrees** | **str** | Site primary contact degrees. | [optional] 
**phone** | **str** | Site primary contact phone number. | [optional] 
**phone_ext** | **str** | Site primary contact phone number extension. | [optional] 
**email** | **str** | Site primary contact email address. | [optional] 
**first_name_backup** | **str** | Site backup contact first name. | [optional] 
**middle_name_backup** | **str** | Site backup contact middle name. | [optional] 
**last_name_backup** | **str** | Site backup contact last name. | [optional] 
**degrees_backup** | **str** | Site backup contact degrees. | [optional] 
**phone_backup** | **str** | Site backup contact phone number. | [optional] 
**phone_ext_backup** | **str** | Site backup contact phone number extension. | [optional] 
**email_backup** | **str** | Site backup contact email address. | [optional] 
**distance** | **float** | Distance based on the distance unit of measure specified (miles if unspecified) from the search location (either geopoint, location object, or inferred search point bsaed on filters provided. | [optional] 
**is_in_institution** | **bool** | If an institutionId was provided for search, indicates if this site is associated with the institution. | [optional] 
**is_in_idn** | **bool** | If an institutionId was provided for search, indicates if this site is associated with the institution&#x27;s Integrated Delivery Network (IDN). | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Concept associations established for this site. | [optional] 



