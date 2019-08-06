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


class AssertionClassifications(object):
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
        'name': 'str',
        'classification': 'str',
        'classification_override': 'str'
    }

    attribute_map = {
        'name': 'name',
        'classification': 'classification',
        'classification_override': 'classificationOverride'
    }

    def __init__(self, name=None, classification=None, classification_override=None):  # noqa: E501
        """AssertionClassifications - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._classification = None
        self._classification_override = None
        self.discriminator = None
        self.name = name
        self.classification = classification
        if classification_override is not None:
            self.classification_override = classification_override

    @property
    def name(self):
        """Gets the name of this AssertionClassifications.  # noqa: E501


        :return: The name of this AssertionClassifications.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssertionClassifications.


        :param name: The name of this AssertionClassifications.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def classification(self):
        """Gets the classification of this AssertionClassifications.  # noqa: E501


        :return: The classification of this AssertionClassifications.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this AssertionClassifications.


        :param classification: The classification of this AssertionClassifications.  # noqa: E501
        :type: str
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")  # noqa: E501
        allowed_values = ["actionable", "unknown", "common", "informative", "germline"]  # noqa: E501
        if classification not in allowed_values:
            raise ValueError(
                "Invalid value for `classification` ({0}), must be one of {1}"  # noqa: E501
                .format(classification, allowed_values)
            )

        self._classification = classification

    @property
    def classification_override(self):
        """Gets the classification_override of this AssertionClassifications.  # noqa: E501


        :return: The classification_override of this AssertionClassifications.  # noqa: E501
        :rtype: str
        """
        return self._classification_override

    @classification_override.setter
    def classification_override(self, classification_override):
        """Sets the classification_override of this AssertionClassifications.


        :param classification_override: The classification_override of this AssertionClassifications.  # noqa: E501
        :type: str
        """
        allowed_values = ["actionable", "unknown", "common", "informative", "germline"]  # noqa: E501
        if classification_override not in allowed_values:
            raise ValueError(
                "Invalid value for `classification_override` ({0}), must be one of {1}"  # noqa: E501
                .format(classification_override, allowed_values)
            )

        self._classification_override = classification_override

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
        if issubclass(AssertionClassifications, dict):
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
        if not isinstance(other, AssertionClassifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
