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


class AssertionSources(object):
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
        'id': 'str',
        'type': 'str',
        'sub_type': 'str',
        'pub_id': 'str',
        'trial_id': 'str',
        'trial_phase': 'str',
        'functional_consequence': 'str',
        'name': 'str',
        'link': 'str',
        'year': 'int',
        'trust_rating': 'float'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'sub_type': 'subType',
        'pub_id': 'pubId',
        'trial_id': 'trialId',
        'trial_phase': 'trialPhase',
        'functional_consequence': 'functionalConsequence',
        'name': 'name',
        'link': 'link',
        'year': 'year',
        'trust_rating': 'trustRating'
    }

    def __init__(self, id=None, type=None, sub_type=None, pub_id=None, trial_id=None, trial_phase=None, functional_consequence=None, name=None, link=None, year=None, trust_rating=None):  # noqa: E501
        """AssertionSources - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._sub_type = None
        self._pub_id = None
        self._trial_id = None
        self._trial_phase = None
        self._functional_consequence = None
        self._name = None
        self._link = None
        self._year = None
        self._trust_rating = None
        self.discriminator = None
        self.id = id
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if pub_id is not None:
            self.pub_id = pub_id
        if trial_id is not None:
            self.trial_id = trial_id
        if trial_phase is not None:
            self.trial_phase = trial_phase
        if functional_consequence is not None:
            self.functional_consequence = functional_consequence
        if name is not None:
            self.name = name
        if link is not None:
            self.link = link
        if year is not None:
            self.year = year
        if trust_rating is not None:
            self.trust_rating = trust_rating

    @property
    def id(self):
        """Gets the id of this AssertionSources.  # noqa: E501

        Unique source identifier for this assertion.  # noqa: E501

        :return: The id of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssertionSources.

        Unique source identifier for this assertion.  # noqa: E501

        :param id: The id of this AssertionSources.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this AssertionSources.  # noqa: E501

        Type of clinical evidence associated with publication.  # noqa: E501

        :return: The type of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssertionSources.

        Type of clinical evidence associated with publication.  # noqa: E501

        :param type: The type of this AssertionSources.  # noqa: E501
        :type: str
        """
        allowed_values = ["trial", "case_study", "preclinical", "expert", "pathway_inferred", "institutional_study", "regulatory", "sequencing", ""]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this AssertionSources.  # noqa: E501

        A more specific sub type of clinical evidence associated with publication.  # noqa: E501

        :return: The sub_type of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this AssertionSources.

        A more specific sub type of clinical evidence associated with publication.  # noqa: E501

        :param sub_type: The sub_type of this AssertionSources.  # noqa: E501
        :type: str
        """
        allowed_values = ["prospective", "retrospective", "meta_analysis", "clinical", "researcher", "cell_line", "pdx", "biochemical_assay", "mouse_model"]  # noqa: E501
        if sub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sub_type, allowed_values)
            )

        self._sub_type = sub_type

    @property
    def pub_id(self):
        """Gets the pub_id of this AssertionSources.  # noqa: E501

        A publication identifier.  # noqa: E501

        :return: The pub_id of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this AssertionSources.

        A publication identifier.  # noqa: E501

        :param pub_id: The pub_id of this AssertionSources.  # noqa: E501
        :type: str
        """

        self._pub_id = pub_id

    @property
    def trial_id(self):
        """Gets the trial_id of this AssertionSources.  # noqa: E501

        A clinical trial identifier.  # noqa: E501

        :return: The trial_id of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._trial_id

    @trial_id.setter
    def trial_id(self, trial_id):
        """Sets the trial_id of this AssertionSources.

        A clinical trial identifier.  # noqa: E501

        :param trial_id: The trial_id of this AssertionSources.  # noqa: E501
        :type: str
        """

        self._trial_id = trial_id

    @property
    def trial_phase(self):
        """Gets the trial_phase of this AssertionSources.  # noqa: E501

        A clinical trial phase.  # noqa: E501

        :return: The trial_phase of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._trial_phase

    @trial_phase.setter
    def trial_phase(self, trial_phase):
        """Sets the trial_phase of this AssertionSources.

        A clinical trial phase.  # noqa: E501

        :param trial_phase: The trial_phase of this AssertionSources.  # noqa: E501
        :type: str
        """

        self._trial_phase = trial_phase

    @property
    def functional_consequence(self):
        """Gets the functional_consequence of this AssertionSources.  # noqa: E501

        Change to function of biomarker.  # noqa: E501

        :return: The functional_consequence of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._functional_consequence

    @functional_consequence.setter
    def functional_consequence(self, functional_consequence):
        """Sets the functional_consequence of this AssertionSources.

        Change to function of biomarker.  # noqa: E501

        :param functional_consequence: The functional_consequence of this AssertionSources.  # noqa: E501
        :type: str
        """
        allowed_values = ["loss_of_function", "gain_of_function", "uncharacterized", "inconclusive"]  # noqa: E501
        if functional_consequence not in allowed_values:
            raise ValueError(
                "Invalid value for `functional_consequence` ({0}), must be one of {1}"  # noqa: E501
                .format(functional_consequence, allowed_values)
            )

        self._functional_consequence = functional_consequence

    @property
    def name(self):
        """Gets the name of this AssertionSources.  # noqa: E501

        Name of publication index if applicable.  # noqa: E501

        :return: The name of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssertionSources.

        Name of publication index if applicable.  # noqa: E501

        :param name: The name of this AssertionSources.  # noqa: E501
        :type: str
        """
        allowed_values = ["PUBMED", "AACR", "ASCO", "ESMO", "ASCOMEETING"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def link(self):
        """Gets the link of this AssertionSources.  # noqa: E501

        A URL to publication if available.  # noqa: E501

        :return: The link of this AssertionSources.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AssertionSources.

        A URL to publication if available.  # noqa: E501

        :param link: The link of this AssertionSources.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def year(self):
        """Gets the year of this AssertionSources.  # noqa: E501

        Year of publication.  # noqa: E501

        :return: The year of this AssertionSources.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this AssertionSources.

        Year of publication.  # noqa: E501

        :param year: The year of this AssertionSources.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def trust_rating(self):
        """Gets the trust_rating of this AssertionSources.  # noqa: E501

        A subjective assessment of evidence quality.  # noqa: E501

        :return: The trust_rating of this AssertionSources.  # noqa: E501
        :rtype: float
        """
        return self._trust_rating

    @trust_rating.setter
    def trust_rating(self, trust_rating):
        """Sets the trust_rating of this AssertionSources.

        A subjective assessment of evidence quality.  # noqa: E501

        :param trust_rating: The trust_rating of this AssertionSources.  # noqa: E501
        :type: float
        """

        self._trust_rating = trust_rating

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
        if issubclass(AssertionSources, dict):
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
        if not isinstance(other, AssertionSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
