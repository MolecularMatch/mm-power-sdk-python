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


class ExternalId(object):
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
        'resource': 'str',
        'identifier': 'str',
        'url': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'identifier': 'identifier',
        'url': 'url'
    }

    def __init__(self, resource=None, identifier=None, url=None):  # noqa: E501
        """ExternalId - a model defined in Swagger"""  # noqa: E501
        self._resource = None
        self._identifier = None
        self._url = None
        self.discriminator = None
        self.resource = resource
        if identifier is not None:
            self.identifier = identifier
        if url is not None:
            self.url = url

    @property
    def resource(self):
        """Gets the resource of this ExternalId.  # noqa: E501

        Name of the source database.  # noqa: E501

        :return: The resource of this ExternalId.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ExternalId.

        Name of the source database.  # noqa: E501

        :param resource: The resource of this ExternalId.  # noqa: E501
        :type: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def identifier(self):
        """Gets the identifier of this ExternalId.  # noqa: E501

        Identifier for this drug in the given resource.  # noqa: E501

        :return: The identifier of this ExternalId.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExternalId.

        Identifier for this drug in the given resource.  # noqa: E501

        :param identifier: The identifier of this ExternalId.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def url(self):
        """Gets the url of this ExternalId.  # noqa: E501

        The URL for this drug in the given resource.  # noqa: E501

        :return: The url of this ExternalId.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ExternalId.

        The URL for this drug in the given resource.  # noqa: E501

        :param url: The url of this ExternalId.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ExternalId, dict):
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
        if not isinstance(other, ExternalId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
