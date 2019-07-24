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


class Eligibility(object):
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
        'gender': 'str',
        'gender_based': 'str',
        'gender_description': 'str',
        'minimum_age': 'str',
        'maximum_age': 'str',
        'healthy_volunteers': 'str',
        'criteria': 'str',
        'study_pop': 'str'
    }

    attribute_map = {
        'gender': 'gender',
        'gender_based': 'gender_based',
        'gender_description': 'gender_description',
        'minimum_age': 'minimum_age',
        'maximum_age': 'maximum_age',
        'healthy_volunteers': 'healthy_volunteers',
        'criteria': 'criteria',
        'study_pop': 'study_pop'
    }

    def __init__(self, gender=None, gender_based=None, gender_description=None, minimum_age=None, maximum_age=None, healthy_volunteers=None, criteria=None, study_pop=None):  # noqa: E501
        """Eligibility - a model defined in Swagger"""  # noqa: E501
        self._gender = None
        self._gender_based = None
        self._gender_description = None
        self._minimum_age = None
        self._maximum_age = None
        self._healthy_volunteers = None
        self._criteria = None
        self._study_pop = None
        self.discriminator = None
        if gender is not None:
            self.gender = gender
        if gender_based is not None:
            self.gender_based = gender_based
        if gender_description is not None:
            self.gender_description = gender_description
        if minimum_age is not None:
            self.minimum_age = minimum_age
        if maximum_age is not None:
            self.maximum_age = maximum_age
        if healthy_volunteers is not None:
            self.healthy_volunteers = healthy_volunteers
        if criteria is not None:
            self.criteria = criteria
        if study_pop is not None:
            self.study_pop = study_pop

    @property
    def gender(self):
        """Gets the gender of this Eligibility.  # noqa: E501


        :return: The gender of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Eligibility.


        :param gender: The gender of this Eligibility.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def gender_based(self):
        """Gets the gender_based of this Eligibility.  # noqa: E501


        :return: The gender_based of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._gender_based

    @gender_based.setter
    def gender_based(self, gender_based):
        """Sets the gender_based of this Eligibility.


        :param gender_based: The gender_based of this Eligibility.  # noqa: E501
        :type: str
        """

        self._gender_based = gender_based

    @property
    def gender_description(self):
        """Gets the gender_description of this Eligibility.  # noqa: E501


        :return: The gender_description of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._gender_description

    @gender_description.setter
    def gender_description(self, gender_description):
        """Sets the gender_description of this Eligibility.


        :param gender_description: The gender_description of this Eligibility.  # noqa: E501
        :type: str
        """

        self._gender_description = gender_description

    @property
    def minimum_age(self):
        """Gets the minimum_age of this Eligibility.  # noqa: E501


        :return: The minimum_age of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, minimum_age):
        """Sets the minimum_age of this Eligibility.


        :param minimum_age: The minimum_age of this Eligibility.  # noqa: E501
        :type: str
        """

        self._minimum_age = minimum_age

    @property
    def maximum_age(self):
        """Gets the maximum_age of this Eligibility.  # noqa: E501


        :return: The maximum_age of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._maximum_age

    @maximum_age.setter
    def maximum_age(self, maximum_age):
        """Sets the maximum_age of this Eligibility.


        :param maximum_age: The maximum_age of this Eligibility.  # noqa: E501
        :type: str
        """

        self._maximum_age = maximum_age

    @property
    def healthy_volunteers(self):
        """Gets the healthy_volunteers of this Eligibility.  # noqa: E501


        :return: The healthy_volunteers of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._healthy_volunteers

    @healthy_volunteers.setter
    def healthy_volunteers(self, healthy_volunteers):
        """Sets the healthy_volunteers of this Eligibility.


        :param healthy_volunteers: The healthy_volunteers of this Eligibility.  # noqa: E501
        :type: str
        """

        self._healthy_volunteers = healthy_volunteers

    @property
    def criteria(self):
        """Gets the criteria of this Eligibility.  # noqa: E501


        :return: The criteria of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this Eligibility.


        :param criteria: The criteria of this Eligibility.  # noqa: E501
        :type: str
        """

        self._criteria = criteria

    @property
    def study_pop(self):
        """Gets the study_pop of this Eligibility.  # noqa: E501


        :return: The study_pop of this Eligibility.  # noqa: E501
        :rtype: str
        """
        return self._study_pop

    @study_pop.setter
    def study_pop(self, study_pop):
        """Sets the study_pop of this Eligibility.


        :param study_pop: The study_pop of this Eligibility.  # noqa: E501
        :type: str
        """

        self._study_pop = study_pop

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
        if issubclass(Eligibility, dict):
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
        if not isinstance(other, Eligibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
