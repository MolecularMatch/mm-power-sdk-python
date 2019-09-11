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


class AssertionPrevalence(object):
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
        'study_id': 'str',
        'percent': 'float',
        'samples': 'int',
        'count': 'int',
        'condition': 'str',
        'molecular': 'str'
    }

    attribute_map = {
        'study_id': 'studyId',
        'percent': 'percent',
        'samples': 'samples',
        'count': 'count',
        'condition': 'condition',
        'molecular': 'molecular'
    }

    def __init__(self, study_id=None, percent=None, samples=None, count=None, condition=None, molecular=None):  # noqa: E501
        """AssertionPrevalence - a model defined in Swagger"""  # noqa: E501
        self._study_id = None
        self._percent = None
        self._samples = None
        self._count = None
        self._condition = None
        self._molecular = None
        self.discriminator = None
        self.study_id = study_id
        self.percent = percent
        self.samples = samples
        self.count = count
        if condition is not None:
            self.condition = condition
        if molecular is not None:
            self.molecular = molecular

    @property
    def study_id(self):
        """Gets the study_id of this AssertionPrevalence.  # noqa: E501

        A study identifier.  # noqa: E501

        :return: The study_id of this AssertionPrevalence.  # noqa: E501
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this AssertionPrevalence.

        A study identifier.  # noqa: E501

        :param study_id: The study_id of this AssertionPrevalence.  # noqa: E501
        :type: str
        """
        if study_id is None:
            raise ValueError("Invalid value for `study_id`, must not be `None`")  # noqa: E501

        self._study_id = study_id

    @property
    def percent(self):
        """Gets the percent of this AssertionPrevalence.  # noqa: E501

        Ratio of people with variant within study population.  # noqa: E501

        :return: The percent of this AssertionPrevalence.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this AssertionPrevalence.

        Ratio of people with variant within study population.  # noqa: E501

        :param percent: The percent of this AssertionPrevalence.  # noqa: E501
        :type: float
        """
        if percent is None:
            raise ValueError("Invalid value for `percent`, must not be `None`")  # noqa: E501

        self._percent = percent

    @property
    def samples(self):
        """Gets the samples of this AssertionPrevalence.  # noqa: E501

        Number of samples with mutation within study.  # noqa: E501

        :return: The samples of this AssertionPrevalence.  # noqa: E501
        :rtype: int
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this AssertionPrevalence.

        Number of samples with mutation within study.  # noqa: E501

        :param samples: The samples of this AssertionPrevalence.  # noqa: E501
        :type: int
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")  # noqa: E501

        self._samples = samples

    @property
    def count(self):
        """Gets the count of this AssertionPrevalence.  # noqa: E501

        Number of occurrances of variant within study.  # noqa: E501

        :return: The count of this AssertionPrevalence.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AssertionPrevalence.

        Number of occurrances of variant within study.  # noqa: E501

        :param count: The count of this AssertionPrevalence.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def condition(self):
        """Gets the condition of this AssertionPrevalence.  # noqa: E501

        The condition associated with the study.  # noqa: E501

        :return: The condition of this AssertionPrevalence.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AssertionPrevalence.

        The condition associated with the study.  # noqa: E501

        :param condition: The condition of this AssertionPrevalence.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def molecular(self):
        """Gets the molecular of this AssertionPrevalence.  # noqa: E501

        The variant associated with the study.  # noqa: E501

        :return: The molecular of this AssertionPrevalence.  # noqa: E501
        :rtype: str
        """
        return self._molecular

    @molecular.setter
    def molecular(self, molecular):
        """Sets the molecular of this AssertionPrevalence.

        The variant associated with the study.  # noqa: E501

        :param molecular: The molecular of this AssertionPrevalence.  # noqa: E501
        :type: str
        """

        self._molecular = molecular

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
        if issubclass(AssertionPrevalence, dict):
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
        if not isinstance(other, AssertionPrevalence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
