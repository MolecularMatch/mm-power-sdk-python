# mm_power_sdk_python
https://molecularmatch.github.io/mm-power-sdk-python/
MMPower API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/MolecularMatch/mm-power-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/MolecularMatch/mm-power-sdk-python.git`)

Then import the package:
```python
import mm_power_sdk_python 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mm_power_sdk_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mm_power_sdk_python
from mm_power_sdk_python.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mm_power_sdk_python.AssertionsApi(mm_power_sdk_python.ApiClient(configuration))
id = 'id_example' # str | ID of the Assertion to return

try:
    # Get an Assertion
    api_response = api_instance.get_assertion(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertionsApi->get_assertion: %s\n" % e)


# create an instance of the API class
api_instance = mm_power_sdk_python.AssertionsApi(mm_power_sdk_python.ApiClient(configuration))
body = mm_power_sdk_python.SearchRequest() # SearchRequest | SearchRequest object to send to MolecularMatch for processing

try:
    # Search for assertions
    api_response = api_instance.search_assertions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssertionsApi->search_assertions: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.molecularmatch.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssertionsApi* | [**get_assertion**](docs/AssertionsApi.md#get_assertion) | **GET** /assertion/{id} | Get an Assertion
*AssertionsApi* | [**search_assertions**](docs/AssertionsApi.md#search_assertions) | **POST** /assertion/search | Search for assertions
*ClinicalTrialsApi* | [**count_trials**](docs/ClinicalTrialsApi.md#count_trials) | **POST** /trial/count | Get the count of Clinical Trials matching a searchRequest
*ClinicalTrialsApi* | [**get_trial**](docs/ClinicalTrialsApi.md#get_trial) | **GET** /trial/{id} | Get a Clinical Trial
*ClinicalTrialsApi* | [**search_trials**](docs/ClinicalTrialsApi.md#search_trials) | **POST** /trial/search | Search for clinical trials
*DrugsApi* | [**get_drug**](docs/DrugsApi.md#get_drug) | **GET** /drug/{id} | Get a Drug
*DrugsApi* | [**search_drugs**](docs/DrugsApi.md#search_drugs) | **POST** /drug/search | Search for drugs
*PublicationApi* | [**count_publications**](docs/PublicationApi.md#count_publications) | **POST** /publication/count | Get the count of Publications matching a searchRequest
*PublicationApi* | [**get_publication**](docs/PublicationApi.md#get_publication) | **GET** /publication/{id} | Get a Publication
*PublicationApi* | [**search_publications**](docs/PublicationApi.md#search_publications) | **POST** /publication/search | Search for Publications

## Documentation For Models

 - [Agency](docs/Agency.md)
 - [ArmGroup](docs/ArmGroup.md)
 - [Assertion](docs/Assertion.md)
 - [AssertionClassifications](docs/AssertionClassifications.md)
 - [AssertionPrevalence](docs/AssertionPrevalence.md)
 - [AssertionSources](docs/AssertionSources.md)
 - [AssertionTherapeuticContext](docs/AssertionTherapeuticContext.md)
 - [ClinicalTrial](docs/ClinicalTrial.md)
 - [ClinicalTrialCountries](docs/ClinicalTrialCountries.md)
 - [ClinicalTrialLocationSummary](docs/ClinicalTrialLocationSummary.md)
 - [ClinicalTrialLocationSummaryCountries](docs/ClinicalTrialLocationSummaryCountries.md)
 - [ClinicalTrialSponsors](docs/ClinicalTrialSponsors.md)
 - [ConceptAssociation](docs/ConceptAssociation.md)
 - [Contact](docs/Contact.md)
 - [Drug](docs/Drug.md)
 - [DrugAvailability](docs/DrugAvailability.md)
 - [DrugBrands](docs/DrugBrands.md)
 - [DrugCompositeTags](docs/DrugCompositeTags.md)
 - [DrugDosages](docs/DrugDosages.md)
 - [DrugDrugclass](docs/DrugDrugclass.md)
 - [DrugParents](docs/DrugParents.md)
 - [DrugPharmacology](docs/DrugPharmacology.md)
 - [DrugPrices](docs/DrugPrices.md)
 - [Eligibility](docs/Eligibility.md)
 - [ExternalId](docs/ExternalId.md)
 - [Facility](docs/Facility.md)
 - [FacilityGeo](docs/FacilityGeo.md)
 - [Filter](docs/Filter.md)
 - [Intervention](docs/Intervention.md)
 - [Outcome](docs/Outcome.md)
 - [Publication](docs/Publication.md)
 - [PublicationAuthors](docs/PublicationAuthors.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchRequestGeopoint](docs/SearchRequestGeopoint.md)
 - [SearchRequestLocation](docs/SearchRequestLocation.md)
 - [SearchRequestMinShouldMatch](docs/SearchRequestMinShouldMatch.md)
 - [SearchResponseAssertion](docs/SearchResponseAssertion.md)
 - [SearchResponseClinicalTrial](docs/SearchResponseClinicalTrial.md)
 - [SearchResponseDrug](docs/SearchResponseDrug.md)
 - [SearchResponsePublication](docs/SearchResponsePublication.md)
 - [StandardizedTier](docs/StandardizedTier.md)
 - [StandardizedTierTier](docs/StandardizedTierTier.md)
 - [StudyDesign](docs/StudyDesign.md)
 - [Synonym](docs/Synonym.md)
 - [Tag](docs/Tag.md)
 - [TierExplanation](docs/TierExplanation.md)
 - [VariantInfo](docs/VariantInfo.md)
 - [VariantInfoFusions](docs/VariantInfoFusions.md)
 - [VariantInfoLocations](docs/VariantInfoLocations.md)

## Documentation For Authorization


## bearerAuth



## Author

support@molecularmatch.com
