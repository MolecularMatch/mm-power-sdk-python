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


class Investigator(object):
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
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'degrees': 'str',
        'role': 'str',
        'affiliation': 'str',
        'phone': 'str',
        'phone_ext': 'str',
        'email': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'degrees': 'degrees',
        'role': 'role',
        'affiliation': 'affiliation',
        'phone': 'phone',
        'phone_ext': 'phone_ext',
        'email': 'email'
    }

    def __init__(self, first_name=None, middle_name=None, last_name=None, degrees=None, role=None, affiliation=None, phone=None, phone_ext=None, email=None):  # noqa: E501
        """Investigator - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._degrees = None
        self._role = None
        self._affiliation = None
        self._phone = None
        self._phone_ext = None
        self._email = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        self.last_name = last_name
        if degrees is not None:
            self.degrees = degrees
        if role is not None:
            self.role = role
        if affiliation is not None:
            self.affiliation = affiliation
        if phone is not None:
            self.phone = phone
        if phone_ext is not None:
            self.phone_ext = phone_ext
        if email is not None:
            self.email = email

    @property
    def first_name(self):
        """Gets the first_name of this Investigator.  # noqa: E501

        First name of the investigator.  # noqa: E501

        :return: The first_name of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Investigator.

        First name of the investigator.  # noqa: E501

        :param first_name: The first_name of this Investigator.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this Investigator.  # noqa: E501

        Middle name of the investigator.  # noqa: E501

        :return: The middle_name of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this Investigator.

        Middle name of the investigator.  # noqa: E501

        :param middle_name: The middle_name of this Investigator.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this Investigator.  # noqa: E501

        Last name of the investigator.  # noqa: E501

        :return: The last_name of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Investigator.

        Last name of the investigator.  # noqa: E501

        :param last_name: The last_name of this Investigator.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def degrees(self):
        """Gets the degrees of this Investigator.  # noqa: E501

        Degress earned by the investigator.  # noqa: E501

        :return: The degrees of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._degrees

    @degrees.setter
    def degrees(self, degrees):
        """Sets the degrees of this Investigator.

        Degress earned by the investigator.  # noqa: E501

        :param degrees: The degrees of this Investigator.  # noqa: E501
        :type: str
        """

        self._degrees = degrees

    @property
    def role(self):
        """Gets the role of this Investigator.  # noqa: E501

        Position or function of the official.  # noqa: E501

        :return: The role of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Investigator.

        Position or function of the official.  # noqa: E501

        :param role: The role of this Investigator.  # noqa: E501
        :type: str
        """
        allowed_values = ["Principal Investigator", "Sub-Investigator", "Study Chair", "Study Director"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def affiliation(self):
        """Gets the affiliation of this Investigator.  # noqa: E501

        Full name of the official's organization.  # noqa: E501

        :return: The affiliation of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        """Sets the affiliation of this Investigator.

        Full name of the official's organization.  # noqa: E501

        :param affiliation: The affiliation of this Investigator.  # noqa: E501
        :type: str
        """

        self._affiliation = affiliation

    @property
    def phone(self):
        """Gets the phone of this Investigator.  # noqa: E501

        Phone number of the investigator.  # noqa: E501

        :return: The phone of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Investigator.

        Phone number of the investigator.  # noqa: E501

        :param phone: The phone of this Investigator.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def phone_ext(self):
        """Gets the phone_ext of this Investigator.  # noqa: E501

        Phone number extension of the investigator.  # noqa: E501

        :return: The phone_ext of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._phone_ext

    @phone_ext.setter
    def phone_ext(self, phone_ext):
        """Sets the phone_ext of this Investigator.

        Phone number extension of the investigator.  # noqa: E501

        :param phone_ext: The phone_ext of this Investigator.  # noqa: E501
        :type: str
        """

        self._phone_ext = phone_ext

    @property
    def email(self):
        """Gets the email of this Investigator.  # noqa: E501

        Electronic mail address of the investigator.  # noqa: E501

        :return: The email of this Investigator.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Investigator.

        Electronic mail address of the investigator.  # noqa: E501

        :param email: The email of this Investigator.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(Investigator, dict):
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
        if not isinstance(other, Investigator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
