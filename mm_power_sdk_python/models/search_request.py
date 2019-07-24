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
from mm_power_sdk_python.models.filter import Filter  # noqa: F401,E501
from mm_power_sdk_python.models.search_request_geopoint import SearchRequestGeopoint  # noqa: F401,E501
from mm_power_sdk_python.models.search_request_location import SearchRequestLocation  # noqa: F401,E501
from mm_power_sdk_python.models.search_request_min_should_match import SearchRequestMinShouldMatch  # noqa: F401,E501


class SearchRequest(object):
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
        'search_key': 'str',
        'institution_id': 'str',
        'case_id': 'str',
        'start': 'int',
        'limit': 'int',
        'location_summary': 'bool',
        'filter_narrative': 'bool',
        'fields': 'list[str]',
        'filters': 'list[Filter]',
        'geopoint': 'SearchRequestGeopoint',
        'location': 'SearchRequestLocation',
        'min_should_match': 'SearchRequestMinShouldMatch'
    }

    attribute_map = {
        'search_key': 'searchKey',
        'institution_id': 'institutionId',
        'case_id': 'caseId',
        'start': 'start',
        'limit': 'limit',
        'location_summary': 'locationSummary',
        'filter_narrative': 'filterNarrative',
        'fields': 'fields',
        'filters': 'filters',
        'geopoint': 'geopoint',
        'location': 'location',
        'min_should_match': 'minShouldMatch'
    }

    def __init__(self, search_key=None, institution_id=None, case_id=None, start=None, limit=20, location_summary=None, filter_narrative=None, fields=None, filters=None, geopoint=None, location=None, min_should_match=None):  # noqa: E501
        """SearchRequest - a model defined in Swagger"""  # noqa: E501
        self._search_key = None
        self._institution_id = None
        self._case_id = None
        self._start = None
        self._limit = None
        self._location_summary = None
        self._filter_narrative = None
        self._fields = None
        self._filters = None
        self._geopoint = None
        self._location = None
        self._min_should_match = None
        self.discriminator = None
        if search_key is not None:
            self.search_key = search_key
        if institution_id is not None:
            self.institution_id = institution_id
        if case_id is not None:
            self.case_id = case_id
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if location_summary is not None:
            self.location_summary = location_summary
        if filter_narrative is not None:
            self.filter_narrative = filter_narrative
        if fields is not None:
            self.fields = fields
        if filters is not None:
            self.filters = filters
        if geopoint is not None:
            self.geopoint = geopoint
        if location is not None:
            self.location = location
        if min_should_match is not None:
            self.min_should_match = min_should_match

    @property
    def search_key(self):
        """Gets the search_key of this SearchRequest.  # noqa: E501

        Search key from a previous response to reconsititute a prior request.  # noqa: E501

        :return: The search_key of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchRequest.

        Search key from a previous response to reconsititute a prior request.  # noqa: E501

        :param search_key: The search_key of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._search_key = search_key

    @property
    def institution_id(self):
        """Gets the institution_id of this SearchRequest.  # noqa: E501

        An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness.  # noqa: E501

        :return: The institution_id of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SearchRequest.

        An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness.  # noqa: E501

        :param institution_id: The institution_id of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def case_id(self):
        """Gets the case_id of this SearchRequest.  # noqa: E501

        For lab specific case tracking.  # noqa: E501

        :return: The case_id of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this SearchRequest.

        For lab specific case tracking.  # noqa: E501

        :param case_id: The case_id of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._case_id = case_id

    @property
    def start(self):
        """Gets the start of this SearchRequest.  # noqa: E501

        Starting record index for paging results.  # noqa: E501

        :return: The start of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SearchRequest.

        Starting record index for paging results.  # noqa: E501

        :param start: The start of this SearchRequest.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def limit(self):
        """Gets the limit of this SearchRequest.  # noqa: E501

        Number of records per page.  # noqa: E501

        :return: The limit of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchRequest.

        Number of records per page.  # noqa: E501

        :param limit: The limit of this SearchRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def location_summary(self):
        """Gets the location_summary of this SearchRequest.  # noqa: E501

        If true, returns a summary location structure instead of the full array of trial locations.  # noqa: E501

        :return: The location_summary of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._location_summary

    @location_summary.setter
    def location_summary(self, location_summary):
        """Sets the location_summary of this SearchRequest.

        If true, returns a summary location structure instead of the full array of trial locations.  # noqa: E501

        :param location_summary: The location_summary of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._location_summary = location_summary

    @property
    def filter_narrative(self):
        """Gets the filter_narrative of this SearchRequest.  # noqa: E501

        If true, include a human readable filter narrative.  # noqa: E501

        :return: The filter_narrative of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._filter_narrative

    @filter_narrative.setter
    def filter_narrative(self, filter_narrative):
        """Sets the filter_narrative of this SearchRequest.

        If true, include a human readable filter narrative.  # noqa: E501

        :param filter_narrative: The filter_narrative of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._filter_narrative = filter_narrative

    @property
    def fields(self):
        """Gets the fields of this SearchRequest.  # noqa: E501

        Provide a field list to customize the return records fields.  # noqa: E501

        :return: The fields of this SearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SearchRequest.

        Provide a field list to customize the return records fields.  # noqa: E501

        :param fields: The fields of this SearchRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def filters(self):
        """Gets the filters of this SearchRequest.  # noqa: E501


        :return: The filters of this SearchRequest.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SearchRequest.


        :param filters: The filters of this SearchRequest.  # noqa: E501
        :type: list[Filter]
        """

        self._filters = filters

    @property
    def geopoint(self):
        """Gets the geopoint of this SearchRequest.  # noqa: E501


        :return: The geopoint of this SearchRequest.  # noqa: E501
        :rtype: SearchRequestGeopoint
        """
        return self._geopoint

    @geopoint.setter
    def geopoint(self, geopoint):
        """Sets the geopoint of this SearchRequest.


        :param geopoint: The geopoint of this SearchRequest.  # noqa: E501
        :type: SearchRequestGeopoint
        """

        self._geopoint = geopoint

    @property
    def location(self):
        """Gets the location of this SearchRequest.  # noqa: E501


        :return: The location of this SearchRequest.  # noqa: E501
        :rtype: SearchRequestLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SearchRequest.


        :param location: The location of this SearchRequest.  # noqa: E501
        :type: SearchRequestLocation
        """

        self._location = location

    @property
    def min_should_match(self):
        """Gets the min_should_match of this SearchRequest.  # noqa: E501


        :return: The min_should_match of this SearchRequest.  # noqa: E501
        :rtype: SearchRequestMinShouldMatch
        """
        return self._min_should_match

    @min_should_match.setter
    def min_should_match(self, min_should_match):
        """Sets the min_should_match of this SearchRequest.


        :param min_should_match: The min_should_match of this SearchRequest.  # noqa: E501
        :type: SearchRequestMinShouldMatch
        """

        self._min_should_match = min_should_match

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
        if issubclass(SearchRequest, dict):
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
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
