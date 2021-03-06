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


class StudyDesign(object):
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
        'allocation': 'str',
        'intervention_model': 'str',
        'intervention_model_description': 'str',
        'primary_purpose': 'str',
        'observational_model': 'str',
        'time_perspective': 'str',
        'masking': 'str',
        'masking_description': 'str'
    }

    attribute_map = {
        'allocation': 'allocation',
        'intervention_model': 'intervention_model',
        'intervention_model_description': 'intervention_model_description',
        'primary_purpose': 'primary_purpose',
        'observational_model': 'observational_model',
        'time_perspective': 'time_perspective',
        'masking': 'masking',
        'masking_description': 'masking_description'
    }

    def __init__(self, allocation=None, intervention_model=None, intervention_model_description=None, primary_purpose=None, observational_model=None, time_perspective=None, masking=None, masking_description=None):  # noqa: E501
        """StudyDesign - a model defined in Swagger"""  # noqa: E501
        self._allocation = None
        self._intervention_model = None
        self._intervention_model_description = None
        self._primary_purpose = None
        self._observational_model = None
        self._time_perspective = None
        self._masking = None
        self._masking_description = None
        self.discriminator = None
        if allocation is not None:
            self.allocation = allocation
        if intervention_model is not None:
            self.intervention_model = intervention_model
        if intervention_model_description is not None:
            self.intervention_model_description = intervention_model_description
        if primary_purpose is not None:
            self.primary_purpose = primary_purpose
        if observational_model is not None:
            self.observational_model = observational_model
        if time_perspective is not None:
            self.time_perspective = time_perspective
        if masking is not None:
            self.masking = masking
        if masking_description is not None:
            self.masking_description = masking_description

    @property
    def allocation(self):
        """Gets the allocation of this StudyDesign.  # noqa: E501

        The method by which participants are assigned to arms in a clinical trial.  # noqa: E501

        :return: The allocation of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this StudyDesign.

        The method by which participants are assigned to arms in a clinical trial.  # noqa: E501

        :param allocation: The allocation of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._allocation = allocation

    @property
    def intervention_model(self):
        """Gets the intervention_model of this StudyDesign.  # noqa: E501

        The strategy for assigning interventions to participants.  # noqa: E501

        :return: The intervention_model of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._intervention_model

    @intervention_model.setter
    def intervention_model(self, intervention_model):
        """Sets the intervention_model of this StudyDesign.

        The strategy for assigning interventions to participants.  # noqa: E501

        :param intervention_model: The intervention_model of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._intervention_model = intervention_model

    @property
    def intervention_model_description(self):
        """Gets the intervention_model_description of this StudyDesign.  # noqa: E501

        Details about the Interventional Study Model.  # noqa: E501

        :return: The intervention_model_description of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._intervention_model_description

    @intervention_model_description.setter
    def intervention_model_description(self, intervention_model_description):
        """Sets the intervention_model_description of this StudyDesign.

        Details about the Interventional Study Model.  # noqa: E501

        :param intervention_model_description: The intervention_model_description of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._intervention_model_description = intervention_model_description

    @property
    def primary_purpose(self):
        """Gets the primary_purpose of this StudyDesign.  # noqa: E501

        The main objective of the intervention(s) being evaluated by the clinical trial.  # noqa: E501

        :return: The primary_purpose of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._primary_purpose

    @primary_purpose.setter
    def primary_purpose(self, primary_purpose):
        """Sets the primary_purpose of this StudyDesign.

        The main objective of the intervention(s) being evaluated by the clinical trial.  # noqa: E501

        :param primary_purpose: The primary_purpose of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._primary_purpose = primary_purpose

    @property
    def observational_model(self):
        """Gets the observational_model of this StudyDesign.  # noqa: E501

        Primary strategy for participant identification and follow-up.  # noqa: E501

        :return: The observational_model of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._observational_model

    @observational_model.setter
    def observational_model(self, observational_model):
        """Sets the observational_model of this StudyDesign.

        Primary strategy for participant identification and follow-up.  # noqa: E501

        :param observational_model: The observational_model of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._observational_model = observational_model

    @property
    def time_perspective(self):
        """Gets the time_perspective of this StudyDesign.  # noqa: E501

        Temporal relationship of observation period to time of participant enrollment.  # noqa: E501

        :return: The time_perspective of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._time_perspective

    @time_perspective.setter
    def time_perspective(self, time_perspective):
        """Sets the time_perspective of this StudyDesign.

        Temporal relationship of observation period to time of participant enrollment.  # noqa: E501

        :param time_perspective: The time_perspective of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._time_perspective = time_perspective

    @property
    def masking(self):
        """Gets the masking of this StudyDesign.  # noqa: E501

        The party or parties involved in the clinical trial who are prevented from having knowledge of the interventions assigned to individual participants.  # noqa: E501

        :return: The masking of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._masking

    @masking.setter
    def masking(self, masking):
        """Sets the masking of this StudyDesign.

        The party or parties involved in the clinical trial who are prevented from having knowledge of the interventions assigned to individual participants.  # noqa: E501

        :param masking: The masking of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._masking = masking

    @property
    def masking_description(self):
        """Gets the masking_description of this StudyDesign.  # noqa: E501

        Information about other parties who may be masked in the clinical trial, if any.  # noqa: E501

        :return: The masking_description of this StudyDesign.  # noqa: E501
        :rtype: str
        """
        return self._masking_description

    @masking_description.setter
    def masking_description(self, masking_description):
        """Sets the masking_description of this StudyDesign.

        Information about other parties who may be masked in the clinical trial, if any.  # noqa: E501

        :param masking_description: The masking_description of this StudyDesign.  # noqa: E501
        :type: str
        """

        self._masking_description = masking_description

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
        if issubclass(StudyDesign, dict):
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
        if not isinstance(other, StudyDesign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
