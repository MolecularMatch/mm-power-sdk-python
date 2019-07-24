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
from mm_power_sdk_python.models.clinical_trial_location_summary_countries import ClinicalTrialLocationSummaryCountries  # noqa: F401,E501


class ClinicalTrialLocationSummary(object):
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
        'us': 'bool',
        'intl': 'bool',
        'count': 'float',
        'recruiting_count': 'float',
        'countries': 'list[ClinicalTrialLocationSummaryCountries]'
    }

    attribute_map = {
        'us': 'us',
        'intl': 'intl',
        'count': 'count',
        'recruiting_count': 'recruitingCount',
        'countries': 'countries'
    }

    def __init__(self, us=None, intl=None, count=None, recruiting_count=None, countries=None):  # noqa: E501
        """ClinicalTrialLocationSummary - a model defined in Swagger"""  # noqa: E501
        self._us = None
        self._intl = None
        self._count = None
        self._recruiting_count = None
        self._countries = None
        self.discriminator = None
        if us is not None:
            self.us = us
        if intl is not None:
            self.intl = intl
        if count is not None:
            self.count = count
        if recruiting_count is not None:
            self.recruiting_count = recruiting_count
        if countries is not None:
            self.countries = countries

    @property
    def us(self):
        """Gets the us of this ClinicalTrialLocationSummary.  # noqa: E501

        Indicates if there are United States based locations.  # noqa: E501

        :return: The us of this ClinicalTrialLocationSummary.  # noqa: E501
        :rtype: bool
        """
        return self._us

    @us.setter
    def us(self, us):
        """Sets the us of this ClinicalTrialLocationSummary.

        Indicates if there are United States based locations.  # noqa: E501

        :param us: The us of this ClinicalTrialLocationSummary.  # noqa: E501
        :type: bool
        """

        self._us = us

    @property
    def intl(self):
        """Gets the intl of this ClinicalTrialLocationSummary.  # noqa: E501

        Indicates if there are locations outside of the United States.  # noqa: E501

        :return: The intl of this ClinicalTrialLocationSummary.  # noqa: E501
        :rtype: bool
        """
        return self._intl

    @intl.setter
    def intl(self, intl):
        """Sets the intl of this ClinicalTrialLocationSummary.

        Indicates if there are locations outside of the United States.  # noqa: E501

        :param intl: The intl of this ClinicalTrialLocationSummary.  # noqa: E501
        :type: bool
        """

        self._intl = intl

    @property
    def count(self):
        """Gets the count of this ClinicalTrialLocationSummary.  # noqa: E501

        The number of trial sites.  # noqa: E501

        :return: The count of this ClinicalTrialLocationSummary.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClinicalTrialLocationSummary.

        The number of trial sites.  # noqa: E501

        :param count: The count of this ClinicalTrialLocationSummary.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def recruiting_count(self):
        """Gets the recruiting_count of this ClinicalTrialLocationSummary.  # noqa: E501

        The number of trial sites that are recruiting patients.  # noqa: E501

        :return: The recruiting_count of this ClinicalTrialLocationSummary.  # noqa: E501
        :rtype: float
        """
        return self._recruiting_count

    @recruiting_count.setter
    def recruiting_count(self, recruiting_count):
        """Sets the recruiting_count of this ClinicalTrialLocationSummary.

        The number of trial sites that are recruiting patients.  # noqa: E501

        :param recruiting_count: The recruiting_count of this ClinicalTrialLocationSummary.  # noqa: E501
        :type: float
        """

        self._recruiting_count = recruiting_count

    @property
    def countries(self):
        """Gets the countries of this ClinicalTrialLocationSummary.  # noqa: E501

        Countries with locations offering this trial.  # noqa: E501

        :return: The countries of this ClinicalTrialLocationSummary.  # noqa: E501
        :rtype: list[ClinicalTrialLocationSummaryCountries]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this ClinicalTrialLocationSummary.

        Countries with locations offering this trial.  # noqa: E501

        :param countries: The countries of this ClinicalTrialLocationSummary.  # noqa: E501
        :type: list[ClinicalTrialLocationSummaryCountries]
        """

        self._countries = countries

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
        if issubclass(ClinicalTrialLocationSummary, dict):
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
        if not isinstance(other, ClinicalTrialLocationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
