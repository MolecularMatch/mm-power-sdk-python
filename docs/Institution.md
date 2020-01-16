# Institution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique identifier. | [optional] 
**name** | **str** | The name of the institution. | 
**country** | **str** | The ISO-3166 2 character country code where the institution is located. | 
**address** | **str** | Number and street portion of the address of the institution. | [optional] 
**sub_division** | **str** | State/Province portion of the address of the institution. | [optional] 
**city** | **str** | City portion of the address of the institution. | [optional] 
**postal_code** | **str** | Postal code portion of the address of the institution. | 
**idn** | **str** | The Integrated Delivery Network (IDN) for this institution.  Provide an id of another institution that is recognized by MoleculatMatch. | [optional] 
**synonyms** | **list[str]** | Alternative names the institution is referred by. | [optional] 
**status** | **str** | Indication of its level of readiness and incorporation into the MolecularMatch Knowledge base. | [optional] 
**test** | **bool** | A flag to mark test institutions. | [optional] 
**expiration_date** | **datetime** | The institution will auto delete on this date.  Only used for institutions marked as test. | [optional] 



