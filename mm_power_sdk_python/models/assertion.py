# coding: utf-8

"""
    MolecularMatch MMPower

    MMPower API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@molecularmatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from mm_power_sdk_python.models.assertion_classifications import AssertionClassifications  # noqa: F401,E501
from mm_power_sdk_python.models.assertion_prevalence import AssertionPrevalence  # noqa: F401,E501
from mm_power_sdk_python.models.assertion_sources import AssertionSources  # noqa: F401,E501
from mm_power_sdk_python.models.assertion_therapeutic_context import AssertionTherapeuticContext  # noqa: F401,E501
from mm_power_sdk_python.models.concept_association import ConceptAssociation  # noqa: F401,E501
from mm_power_sdk_python.models.tier_explanation import TierExplanation  # noqa: F401,E501
from mm_power_sdk_python.models.variant_info import VariantInfo  # noqa: F401,E501


class Assertion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'score': 'float',
        'id': 'str',
        'external_id': 'list[str]',
        'unique_key': 'str',
        'hash_key': 'str',
        'description': 'str',
        'narrative': 'str',
        'regulatory_body': 'str',
        'customer': 'str',
        'version': 'int',
        'regulatory_body_approved': 'bool',
        'regulatory_body_approved_by': 'str',
        'direction': 'str',
        'guideline_body': 'str',
        'guideline_version': 'str',
        'clinical_significance': 'str',
        'biomarker_class': 'str',
        'expression': 'str',
        'sources': 'list[AssertionSources]',
        'no_therapy_available': 'bool',
        'therapeutic_context': 'list[AssertionTherapeuticContext]',
        'tier': 'str',
        'tier_explanation': 'list[TierExplanation]',
        'criteria_unmet': 'list[ConceptAssociation]',
        'criteria_met': 'list[ConceptAssociation]',
        'classifications': 'list[AssertionClassifications]',
        'prevalence': 'list[AssertionPrevalence]',
        'variant_info': 'list[VariantInfo]'
    }

    attribute_map = {
        'score': '_score',
        'id': 'id',
        'external_id': 'external_id',
        'unique_key': 'uniqueKey',
        'hash_key': 'hashKey',
        'description': 'description',
        'narrative': 'narrative',
        'regulatory_body': 'regulatoryBody',
        'customer': 'customer',
        'version': 'version',
        'regulatory_body_approved': 'regulatoryBodyApproved',
        'regulatory_body_approved_by': 'regulatoryBodyApprovedBy',
        'direction': 'direction',
        'guideline_body': 'guidelineBody',
        'guideline_version': 'guidelineVersion',
        'clinical_significance': 'clinicalSignificance',
        'biomarker_class': 'biomarkerClass',
        'expression': 'expression',
        'sources': 'sources',
        'no_therapy_available': 'noTherapyAvailable',
        'therapeutic_context': 'therapeuticContext',
        'tier': 'tier',
        'tier_explanation': 'tierExplanation',
        'criteria_unmet': 'criteriaUnmet',
        'criteria_met': 'criteriaMet',
        'classifications': 'classifications',
        'prevalence': 'prevalence',
        'variant_info': 'variantInfo'
    }

    def __init__(self, score=None, id=None, external_id=None, unique_key=None, hash_key=None, description=None, narrative=None, regulatory_body=None, customer=None, version=None, regulatory_body_approved=None, regulatory_body_approved_by=None, direction=None, guideline_body=None, guideline_version=None, clinical_significance=None, biomarker_class=None, expression=None, sources=None, no_therapy_available=None, therapeutic_context=None, tier=None, tier_explanation=None, criteria_unmet=None, criteria_met=None, classifications=None, prevalence=None, variant_info=None):  # noqa: E501
        """Assertion - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._id = None
        self._external_id = None
        self._unique_key = None
        self._hash_key = None
        self._description = None
        self._narrative = None
        self._regulatory_body = None
        self._customer = None
        self._version = None
        self._regulatory_body_approved = None
        self._regulatory_body_approved_by = None
        self._direction = None
        self._guideline_body = None
        self._guideline_version = None
        self._clinical_significance = None
        self._biomarker_class = None
        self._expression = None
        self._sources = None
        self._no_therapy_available = None
        self._therapeutic_context = None
        self._tier = None
        self._tier_explanation = None
        self._criteria_unmet = None
        self._criteria_met = None
        self._classifications = None
        self._prevalence = None
        self._variant_info = None
        self.discriminator = None
        if score is not None:
            self.score = score
        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        if unique_key is not None:
            self.unique_key = unique_key
        if hash_key is not None:
            self.hash_key = hash_key
        if description is not None:
            self.description = description
        if narrative is not None:
            self.narrative = narrative
        self.regulatory_body = regulatory_body
        self.customer = customer
        self.version = version
        if regulatory_body_approved is not None:
            self.regulatory_body_approved = regulatory_body_approved
        if regulatory_body_approved_by is not None:
            self.regulatory_body_approved_by = regulatory_body_approved_by
        if direction is not None:
            self.direction = direction
        if guideline_body is not None:
            self.guideline_body = guideline_body
        if guideline_version is not None:
            self.guideline_version = guideline_version
        if clinical_significance is not None:
            self.clinical_significance = clinical_significance
        if biomarker_class is not None:
            self.biomarker_class = biomarker_class
        if expression is not None:
            self.expression = expression
        if sources is not None:
            self.sources = sources
        if no_therapy_available is not None:
            self.no_therapy_available = no_therapy_available
        if therapeutic_context is not None:
            self.therapeutic_context = therapeutic_context
        if tier is not None:
            self.tier = tier
        if tier_explanation is not None:
            self.tier_explanation = tier_explanation
        if criteria_unmet is not None:
            self.criteria_unmet = criteria_unmet
        if criteria_met is not None:
            self.criteria_met = criteria_met
        if classifications is not None:
            self.classifications = classifications
        if prevalence is not None:
            self.prevalence = prevalence
        if variant_info is not None:
            self.variant_info = variant_info

    @property
    def score(self):
        """Gets the score of this Assertion.  # noqa: E501

        indicator of the quality of the match.  # noqa: E501

        :return: The score of this Assertion.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Assertion.

        indicator of the quality of the match.  # noqa: E501

        :param score: The score of this Assertion.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def id(self):
        """Gets the id of this Assertion.  # noqa: E501


        :return: The id of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Assertion.


        :param id: The id of this Assertion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Assertion.  # noqa: E501

        Optional institution specific identifier.  # noqa: E501

        :return: The external_id of this Assertion.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Assertion.

        Optional institution specific identifier.  # noqa: E501

        :param external_id: The external_id of this Assertion.  # noqa: E501
        :type: list[str]
        """

        self._external_id = external_id

    @property
    def unique_key(self):
        """Gets the unique_key of this Assertion.  # noqa: E501

        Unique identifer inclusive of version.  # noqa: E501

        :return: The unique_key of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """Sets the unique_key of this Assertion.

        Unique identifer inclusive of version.  # noqa: E501

        :param unique_key: The unique_key of this Assertion.  # noqa: E501
        :type: str
        """

        self._unique_key = unique_key

    @property
    def hash_key(self):
        """Gets the hash_key of this Assertion.  # noqa: E501

        Static identifier agnostic of version.  # noqa: E501

        :return: The hash_key of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._hash_key

    @hash_key.setter
    def hash_key(self, hash_key):
        """Sets the hash_key of this Assertion.

        Static identifier agnostic of version.  # noqa: E501

        :param hash_key: The hash_key of this Assertion.  # noqa: E501
        :type: str
        """

        self._hash_key = hash_key

    @property
    def description(self):
        """Gets the description of this Assertion.  # noqa: E501

        Detailed description of the assertion.  # noqa: E501

        :return: The description of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Assertion.

        Detailed description of the assertion.  # noqa: E501

        :param description: The description of this Assertion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def narrative(self):
        """Gets the narrative of this Assertion.  # noqa: E501

        A human readeable narrative describing the assertion.  # noqa: E501

        :return: The narrative of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._narrative

    @narrative.setter
    def narrative(self, narrative):
        """Sets the narrative of this Assertion.

        A human readeable narrative describing the assertion.  # noqa: E501

        :param narrative: The narrative of this Assertion.  # noqa: E501
        :type: str
        """

        self._narrative = narrative

    @property
    def regulatory_body(self):
        """Gets the regulatory_body of this Assertion.  # noqa: E501

        The regulatory body that has governance over this assertion.  # noqa: E501

        :return: The regulatory_body of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._regulatory_body

    @regulatory_body.setter
    def regulatory_body(self, regulatory_body):
        """Sets the regulatory_body of this Assertion.

        The regulatory body that has governance over this assertion.  # noqa: E501

        :param regulatory_body: The regulatory_body of this Assertion.  # noqa: E501
        :type: str
        """
        if regulatory_body is None:
            raise ValueError("Invalid value for `regulatory_body`, must not be `None`")  # noqa: E501
        allowed_values = ["FDA", "EMA", "HCA", "TGA"]  # noqa: E501
        if regulatory_body not in allowed_values:
            raise ValueError(
                "Invalid value for `regulatory_body` ({0}), must be one of {1}"  # noqa: E501
                .format(regulatory_body, allowed_values)
            )

        self._regulatory_body = regulatory_body

    @property
    def customer(self):
        """Gets the customer of this Assertion.  # noqa: E501

        The customer identifier that has governance over this assertion.  # noqa: E501

        :return: The customer of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Assertion.

        The customer identifier that has governance over this assertion.  # noqa: E501

        :param customer: The customer of this Assertion.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def version(self):
        """Gets the version of this Assertion.  # noqa: E501

        The assertion set version number.  # noqa: E501

        :return: The version of this Assertion.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Assertion.

        The assertion set version number.  # noqa: E501

        :param version: The version of this Assertion.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def regulatory_body_approved(self):
        """Gets the regulatory_body_approved of this Assertion.  # noqa: E501

        If true, this assertion's therapuetic context has regulatory approval.  # noqa: E501

        :return: The regulatory_body_approved of this Assertion.  # noqa: E501
        :rtype: bool
        """
        return self._regulatory_body_approved

    @regulatory_body_approved.setter
    def regulatory_body_approved(self, regulatory_body_approved):
        """Sets the regulatory_body_approved of this Assertion.

        If true, this assertion's therapuetic context has regulatory approval.  # noqa: E501

        :param regulatory_body_approved: The regulatory_body_approved of this Assertion.  # noqa: E501
        :type: bool
        """

        self._regulatory_body_approved = regulatory_body_approved

    @property
    def regulatory_body_approved_by(self):
        """Gets the regulatory_body_approved_by of this Assertion.  # noqa: E501

        Governing body granting approval.  # noqa: E501

        :return: The regulatory_body_approved_by of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._regulatory_body_approved_by

    @regulatory_body_approved_by.setter
    def regulatory_body_approved_by(self, regulatory_body_approved_by):
        """Sets the regulatory_body_approved_by of this Assertion.

        Governing body granting approval.  # noqa: E501

        :param regulatory_body_approved_by: The regulatory_body_approved_by of this Assertion.  # noqa: E501
        :type: str
        """

        self._regulatory_body_approved_by = regulatory_body_approved_by

    @property
    def direction(self):
        """Gets the direction of this Assertion.  # noqa: E501

        Indicates whether assertion supports or does not support the therapy.  # noqa: E501

        :return: The direction of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Assertion.

        Indicates whether assertion supports or does not support the therapy.  # noqa: E501

        :param direction: The direction of this Assertion.  # noqa: E501
        :type: str
        """
        allowed_values = ["supports", "does_not_support"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def guideline_body(self):
        """Gets the guideline_body of this Assertion.  # noqa: E501

        A professional committee recommendation.  # noqa: E501

        :return: The guideline_body of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._guideline_body

    @guideline_body.setter
    def guideline_body(self, guideline_body):
        """Sets the guideline_body of this Assertion.

        A professional committee recommendation.  # noqa: E501

        :param guideline_body: The guideline_body of this Assertion.  # noqa: E501
        :type: str
        """
        allowed_values = ["NCCN", "ASCO", "ESMO", "AJCC", "AMP", "CAP"]  # noqa: E501
        if guideline_body not in allowed_values:
            raise ValueError(
                "Invalid value for `guideline_body` ({0}), must be one of {1}"  # noqa: E501
                .format(guideline_body, allowed_values)
            )

        self._guideline_body = guideline_body

    @property
    def guideline_version(self):
        """Gets the guideline_version of this Assertion.  # noqa: E501

        Release version of professional committee recommendation.  # noqa: E501

        :return: The guideline_version of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._guideline_version

    @guideline_version.setter
    def guideline_version(self, guideline_version):
        """Sets the guideline_version of this Assertion.

        Release version of professional committee recommendation.  # noqa: E501

        :param guideline_version: The guideline_version of this Assertion.  # noqa: E501
        :type: str
        """

        self._guideline_version = guideline_version

    @property
    def clinical_significance(self):
        """Gets the clinical_significance of this Assertion.  # noqa: E501

        Utility of biomarker in clinical setting.  # noqa: E501

        :return: The clinical_significance of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._clinical_significance

    @clinical_significance.setter
    def clinical_significance(self, clinical_significance):
        """Sets the clinical_significance of this Assertion.

        Utility of biomarker in clinical setting.  # noqa: E501

        :param clinical_significance: The clinical_significance of this Assertion.  # noqa: E501
        :type: str
        """
        allowed_values = ["no_response", "sensitive", "favorable", "unfavorable", "unknown", "resistant", "intermediate", "adverse_response", "pathogenic"]  # noqa: E501
        if clinical_significance not in allowed_values:
            raise ValueError(
                "Invalid value for `clinical_significance` ({0}), must be one of {1}"  # noqa: E501
                .format(clinical_significance, allowed_values)
            )

        self._clinical_significance = clinical_significance

    @property
    def biomarker_class(self):
        """Gets the biomarker_class of this Assertion.  # noqa: E501

        Indicator of response to therapy  # noqa: E501

        :return: The biomarker_class of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._biomarker_class

    @biomarker_class.setter
    def biomarker_class(self, biomarker_class):
        """Sets the biomarker_class of this Assertion.

        Indicator of response to therapy  # noqa: E501

        :param biomarker_class: The biomarker_class of this Assertion.  # noqa: E501
        :type: str
        """
        allowed_values = ["predictive", "diagnostic", "prognostic", "unknown", "predisposing"]  # noqa: E501
        if biomarker_class not in allowed_values:
            raise ValueError(
                "Invalid value for `biomarker_class` ({0}), must be one of {1}"  # noqa: E501
                .format(biomarker_class, allowed_values)
            )

        self._biomarker_class = biomarker_class

    @property
    def expression(self):
        """Gets the expression of this Assertion.  # noqa: E501

        mathematical expression characterizing the clinical scope of the assertion.  # noqa: E501

        :return: The expression of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Assertion.

        mathematical expression characterizing the clinical scope of the assertion.  # noqa: E501

        :param expression: The expression of this Assertion.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def sources(self):
        """Gets the sources of this Assertion.  # noqa: E501

        The supporting evidence for this assertion.  # noqa: E501

        :return: The sources of this Assertion.  # noqa: E501
        :rtype: list[AssertionSources]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Assertion.

        The supporting evidence for this assertion.  # noqa: E501

        :param sources: The sources of this Assertion.  # noqa: E501
        :type: list[AssertionSources]
        """

        self._sources = sources

    @property
    def no_therapy_available(self):
        """Gets the no_therapy_available of this Assertion.  # noqa: E501

        If true, there is no therapy related to this assertion.  # noqa: E501

        :return: The no_therapy_available of this Assertion.  # noqa: E501
        :rtype: bool
        """
        return self._no_therapy_available

    @no_therapy_available.setter
    def no_therapy_available(self, no_therapy_available):
        """Sets the no_therapy_available of this Assertion.

        If true, there is no therapy related to this assertion.  # noqa: E501

        :param no_therapy_available: The no_therapy_available of this Assertion.  # noqa: E501
        :type: bool
        """

        self._no_therapy_available = no_therapy_available

    @property
    def therapeutic_context(self):
        """Gets the therapeutic_context of this Assertion.  # noqa: E501

        The therapies associated with this assertion.  # noqa: E501

        :return: The therapeutic_context of this Assertion.  # noqa: E501
        :rtype: list[AssertionTherapeuticContext]
        """
        return self._therapeutic_context

    @therapeutic_context.setter
    def therapeutic_context(self, therapeutic_context):
        """Sets the therapeutic_context of this Assertion.

        The therapies associated with this assertion.  # noqa: E501

        :param therapeutic_context: The therapeutic_context of this Assertion.  # noqa: E501
        :type: list[AssertionTherapeuticContext]
        """

        self._therapeutic_context = therapeutic_context

    @property
    def tier(self):
        """Gets the tier of this Assertion.  # noqa: E501

        The tiering template specific tier associated with the therapy.  # noqa: E501

        :return: The tier of this Assertion.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this Assertion.

        The tiering template specific tier associated with the therapy.  # noqa: E501

        :param tier: The tier of this Assertion.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def tier_explanation(self):
        """Gets the tier_explanation of this Assertion.  # noqa: E501

        The explanation of how the tier was calculated.  # noqa: E501

        :return: The tier_explanation of this Assertion.  # noqa: E501
        :rtype: list[TierExplanation]
        """
        return self._tier_explanation

    @tier_explanation.setter
    def tier_explanation(self, tier_explanation):
        """Sets the tier_explanation of this Assertion.

        The explanation of how the tier was calculated.  # noqa: E501

        :param tier_explanation: The tier_explanation of this Assertion.  # noqa: E501
        :type: list[TierExplanation]
        """

        self._tier_explanation = tier_explanation

    @property
    def criteria_unmet(self):
        """Gets the criteria_unmet of this Assertion.  # noqa: E501


        :return: The criteria_unmet of this Assertion.  # noqa: E501
        :rtype: list[ConceptAssociation]
        """
        return self._criteria_unmet

    @criteria_unmet.setter
    def criteria_unmet(self, criteria_unmet):
        """Sets the criteria_unmet of this Assertion.


        :param criteria_unmet: The criteria_unmet of this Assertion.  # noqa: E501
        :type: list[ConceptAssociation]
        """

        self._criteria_unmet = criteria_unmet

    @property
    def criteria_met(self):
        """Gets the criteria_met of this Assertion.  # noqa: E501


        :return: The criteria_met of this Assertion.  # noqa: E501
        :rtype: list[ConceptAssociation]
        """
        return self._criteria_met

    @criteria_met.setter
    def criteria_met(self, criteria_met):
        """Sets the criteria_met of this Assertion.


        :param criteria_met: The criteria_met of this Assertion.  # noqa: E501
        :type: list[ConceptAssociation]
        """

        self._criteria_met = criteria_met

    @property
    def classifications(self):
        """Gets the classifications of this Assertion.  # noqa: E501


        :return: The classifications of this Assertion.  # noqa: E501
        :rtype: list[AssertionClassifications]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this Assertion.


        :param classifications: The classifications of this Assertion.  # noqa: E501
        :type: list[AssertionClassifications]
        """

        self._classifications = classifications

    @property
    def prevalence(self):
        """Gets the prevalence of this Assertion.  # noqa: E501


        :return: The prevalence of this Assertion.  # noqa: E501
        :rtype: list[AssertionPrevalence]
        """
        return self._prevalence

    @prevalence.setter
    def prevalence(self, prevalence):
        """Sets the prevalence of this Assertion.


        :param prevalence: The prevalence of this Assertion.  # noqa: E501
        :type: list[AssertionPrevalence]
        """

        self._prevalence = prevalence

    @property
    def variant_info(self):
        """Gets the variant_info of this Assertion.  # noqa: E501

        Genomic information pertaining to variant.  # noqa: E501

        :return: The variant_info of this Assertion.  # noqa: E501
        :rtype: list[VariantInfo]
        """
        return self._variant_info

    @variant_info.setter
    def variant_info(self, variant_info):
        """Sets the variant_info of this Assertion.

        Genomic information pertaining to variant.  # noqa: E501

        :param variant_info: The variant_info of this Assertion.  # noqa: E501
        :type: list[VariantInfo]
        """

        self._variant_info = variant_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Assertion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Assertion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
