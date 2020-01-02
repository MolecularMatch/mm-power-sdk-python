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


class ExpandedAccess(object):
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
        'expanded_access_type_individual': 'bool',
        'expanded_access_type_intermediate': 'bool',
        'expanded_access_type_treatment': 'bool'
    }

    attribute_map = {
        'expanded_access_type_individual': 'expanded_access_type_individual',
        'expanded_access_type_intermediate': 'expanded_access_type_intermediate',
        'expanded_access_type_treatment': 'expanded_access_type_treatment'
    }

    def __init__(self, expanded_access_type_individual=None, expanded_access_type_intermediate=None, expanded_access_type_treatment=None):  # noqa: E501
        """ExpandedAccess - a model defined in Swagger"""  # noqa: E501
        self._expanded_access_type_individual = None
        self._expanded_access_type_intermediate = None
        self._expanded_access_type_treatment = None
        self.discriminator = None
        if expanded_access_type_individual is not None:
            self.expanded_access_type_individual = expanded_access_type_individual
        if expanded_access_type_intermediate is not None:
            self.expanded_access_type_intermediate = expanded_access_type_intermediate
        if expanded_access_type_treatment is not None:
            self.expanded_access_type_treatment = expanded_access_type_treatment

    @property
    def expanded_access_type_individual(self):
        """Gets the expanded_access_type_individual of this ExpandedAccess.  # noqa: E501

        Individual Patients: For individual participants, including for emergency use, as specified in 21 CFR 312.310.  # noqa: E501

        :return: The expanded_access_type_individual of this ExpandedAccess.  # noqa: E501
        :rtype: bool
        """
        return self._expanded_access_type_individual

    @expanded_access_type_individual.setter
    def expanded_access_type_individual(self, expanded_access_type_individual):
        """Sets the expanded_access_type_individual of this ExpandedAccess.

        Individual Patients: For individual participants, including for emergency use, as specified in 21 CFR 312.310.  # noqa: E501

        :param expanded_access_type_individual: The expanded_access_type_individual of this ExpandedAccess.  # noqa: E501
        :type: bool
        """

        self._expanded_access_type_individual = expanded_access_type_individual

    @property
    def expanded_access_type_intermediate(self):
        """Gets the expanded_access_type_intermediate of this ExpandedAccess.  # noqa: E501

        Intermediate-size Population: For intermediate-size participant populations, as specified in 21 CFR 312.315.  # noqa: E501

        :return: The expanded_access_type_intermediate of this ExpandedAccess.  # noqa: E501
        :rtype: bool
        """
        return self._expanded_access_type_intermediate

    @expanded_access_type_intermediate.setter
    def expanded_access_type_intermediate(self, expanded_access_type_intermediate):
        """Sets the expanded_access_type_intermediate of this ExpandedAccess.

        Intermediate-size Population: For intermediate-size participant populations, as specified in 21 CFR 312.315.  # noqa: E501

        :param expanded_access_type_intermediate: The expanded_access_type_intermediate of this ExpandedAccess.  # noqa: E501
        :type: bool
        """

        self._expanded_access_type_intermediate = expanded_access_type_intermediate

    @property
    def expanded_access_type_treatment(self):
        """Gets the expanded_access_type_treatment of this ExpandedAccess.  # noqa: E501

        Treatment IND/Protocol: Under a treatment IND or treatment protocol, as specified in 21 CFR 312.320.  # noqa: E501

        :return: The expanded_access_type_treatment of this ExpandedAccess.  # noqa: E501
        :rtype: bool
        """
        return self._expanded_access_type_treatment

    @expanded_access_type_treatment.setter
    def expanded_access_type_treatment(self, expanded_access_type_treatment):
        """Sets the expanded_access_type_treatment of this ExpandedAccess.

        Treatment IND/Protocol: Under a treatment IND or treatment protocol, as specified in 21 CFR 312.320.  # noqa: E501

        :param expanded_access_type_treatment: The expanded_access_type_treatment of this ExpandedAccess.  # noqa: E501
        :type: bool
        """

        self._expanded_access_type_treatment = expanded_access_type_treatment

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
        if issubclass(ExpandedAccess, dict):
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
        if not isinstance(other, ExpandedAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
