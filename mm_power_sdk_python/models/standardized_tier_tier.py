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


class StandardizedTierTier(object):
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
        'value': 'str',
        'calculated_at': 'datetime',
        'explanation': 'list[TierExplanation]'
    }

    attribute_map = {
        'value': 'value',
        'calculated_at': 'calculatedAt',
        'explanation': 'explanation'
    }

    def __init__(self, value=None, calculated_at=None, explanation=None):  # noqa: E501
        """StandardizedTierTier - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._calculated_at = None
        self._explanation = None
        self.discriminator = None
        self.value = value
        if calculated_at is not None:
            self.calculated_at = calculated_at
        if explanation is not None:
            self.explanation = explanation

    @property
    def value(self):
        """Gets the value of this StandardizedTierTier.  # noqa: E501


        :return: The value of this StandardizedTierTier.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StandardizedTierTier.


        :param value: The value of this StandardizedTierTier.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def calculated_at(self):
        """Gets the calculated_at of this StandardizedTierTier.  # noqa: E501


        :return: The calculated_at of this StandardizedTierTier.  # noqa: E501
        :rtype: datetime
        """
        return self._calculated_at

    @calculated_at.setter
    def calculated_at(self, calculated_at):
        """Sets the calculated_at of this StandardizedTierTier.


        :param calculated_at: The calculated_at of this StandardizedTierTier.  # noqa: E501
        :type: datetime
        """

        self._calculated_at = calculated_at

    @property
    def explanation(self):
        """Gets the explanation of this StandardizedTierTier.  # noqa: E501


        :return: The explanation of this StandardizedTierTier.  # noqa: E501
        :rtype: list[TierExplanation]
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this StandardizedTierTier.


        :param explanation: The explanation of this StandardizedTierTier.  # noqa: E501
        :type: list[TierExplanation]
        """

        self._explanation = explanation

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
        if issubclass(StandardizedTierTier, dict):
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
        if not isinstance(other, StandardizedTierTier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
