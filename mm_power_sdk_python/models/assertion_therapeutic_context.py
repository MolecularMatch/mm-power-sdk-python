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


class AssertionTherapeuticContext(object):
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
        'facet': 'str'
    }

    attribute_map = {
        'name': 'name',
        'facet': 'facet'
    }

    def __init__(self, name=None, facet=None):  # noqa: E501
        """AssertionTherapeuticContext - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._facet = None
        self.discriminator = None
        self.name = name
        self.facet = facet

    @property
    def name(self):
        """Gets the name of this AssertionTherapeuticContext.  # noqa: E501

        Drug name.  # noqa: E501

        :return: The name of this AssertionTherapeuticContext.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssertionTherapeuticContext.

        Drug name.  # noqa: E501

        :param name: The name of this AssertionTherapeuticContext.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def facet(self):
        """Gets the facet of this AssertionTherapeuticContext.  # noqa: E501


        :return: The facet of this AssertionTherapeuticContext.  # noqa: E501
        :rtype: str
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this AssertionTherapeuticContext.


        :param facet: The facet of this AssertionTherapeuticContext.  # noqa: E501
        :type: str
        """
        if facet is None:
            raise ValueError("Invalid value for `facet`, must not be `None`")  # noqa: E501

        self._facet = facet

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
        if issubclass(AssertionTherapeuticContext, dict):
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
        if not isinstance(other, AssertionTherapeuticContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
