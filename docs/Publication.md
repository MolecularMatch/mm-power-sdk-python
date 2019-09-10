# Publication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | indicator of the quality of the match. | [optional] 
**mboost** | **float** | intrinsic boost to the record. | [optional] 
**id** | **str** | unique identifier. | 
**pmid** | **str** | PubMed ID. | [optional] 
**doi** | **str** | Digital Object Identifier (permanent link at doi.org/[doi]). | [optional] 
**source** | **str** | data source of this record | 
**journal_name** | **str** | Journal name. | 
**journal_iso_abbreviation** | **str** |  | [optional] 
**title** | **str** | Official title for the publication. | 
**purpose** | **str** | Abstract&#x27;s purpose section. | [optional] 
**background** | **str** | Abstract&#x27;s background section. | [optional] 
**methods** | **str** | Abstract&#x27;s methods section. | [optional] 
**results** | **str** | Abstract&#x27;s results section. | [optional] 
**conclusion** | **str** | Abstract&#x27;s conclusion section. | [optional] 
**conflicts** | **str** | Author&#x27;s conflicts of interest section. | [optional] 
**fulltext** | **str** | Full text (if available). | [optional] 
**citation** | **str** | MLA formatted citation. | 
**citation_date** | **datetime** | Article date used for citation | 
**link** | **str** | Link to original source. | [optional] 
**chemicals** | **list[str]** | Chemicals or drugs referenced in this publication. | [optional] 
**keywords** | **list[str]** |  | [optional] 
**extended_keywords** | **list[str]** |  | [optional] 
**publication_type** | **list[str]** | Publication types infered by MM. | [optional] 
**authors** | [**list[PublicationAuthors]**](PublicationAuthors.md) |  | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Concept associations established for this publication. | [optional] 
**molecular_alterations** | [**list[ConceptAssociation]**](ConceptAssociation.md) | Molecular concept associations established for this publication. | [optional] 



