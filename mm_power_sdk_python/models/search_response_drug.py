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


class SearchResponseDrug(object):
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
        'tiering_template': 'str',
        'tiering_template_legend': 'object',
        'total': 'int',
        'total_pages': 'int',
        'page': 'int',
        'rows': 'list[Drug]',
        'rationalized': 'list[Filter]',
        'unrecognized': 'list[Filter]',
        'filter_narrative': 'str',
        'ambiguous_narrative': 'list[str]'
    }

    attribute_map = {
        'search_key': 'searchKey',
        'institution_id': 'institutionId',
        'case_id': 'caseId',
        'tiering_template': 'tieringTemplate',
        'tiering_template_legend': 'tieringTemplateLegend',
        'total': 'total',
        'total_pages': 'totalPages',
        'page': 'page',
        'rows': 'rows',
        'rationalized': 'rationalized',
        'unrecognized': 'unrecognized',
        'filter_narrative': 'filterNarrative',
        'ambiguous_narrative': 'ambiguousNarrative'
    }

    def __init__(self, search_key=None, institution_id=None, case_id=None, tiering_template=None, tiering_template_legend=None, total=None, total_pages=None, page=None, rows=None, rationalized=None, unrecognized=None, filter_narrative=None, ambiguous_narrative=None):  # noqa: E501
        """SearchResponseDrug - a model defined in Swagger"""  # noqa: E501
        self._search_key = None
        self._institution_id = None
        self._case_id = None
        self._tiering_template = None
        self._tiering_template_legend = None
        self._total = None
        self._total_pages = None
        self._page = None
        self._rows = None
        self._rationalized = None
        self._unrecognized = None
        self._filter_narrative = None
        self._ambiguous_narrative = None
        self.discriminator = None
        if search_key is not None:
            self.search_key = search_key
        if institution_id is not None:
            self.institution_id = institution_id
        if case_id is not None:
            self.case_id = case_id
        self.tiering_template = tiering_template
        if tiering_template_legend is not None:
            self.tiering_template_legend = tiering_template_legend
        self.total = total
        self.total_pages = total_pages
        self.page = page
        if rows is not None:
            self.rows = rows
        if rationalized is not None:
            self.rationalized = rationalized
        if unrecognized is not None:
            self.unrecognized = unrecognized
        if filter_narrative is not None:
            self.filter_narrative = filter_narrative
        if ambiguous_narrative is not None:
            self.ambiguous_narrative = ambiguous_narrative

    @property
    def search_key(self):
        """Gets the search_key of this SearchResponseDrug.  # noqa: E501

        Search key from a previous response to reconsititute a prior request.  # noqa: E501

        :return: The search_key of this SearchResponseDrug.  # noqa: E501
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchResponseDrug.

        Search key from a previous response to reconsititute a prior request.  # noqa: E501

        :param search_key: The search_key of this SearchResponseDrug.  # noqa: E501
        :type: str
        """

        self._search_key = search_key

    @property
    def institution_id(self):
        """Gets the institution_id of this SearchResponseDrug.  # noqa: E501

        An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness.  # noqa: E501

        :return: The institution_id of this SearchResponseDrug.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SearchResponseDrug.

        An institution identifier recognized by MolecularMatch to enable institution specific results and location awareness.  # noqa: E501

        :param institution_id: The institution_id of this SearchResponseDrug.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def case_id(self):
        """Gets the case_id of this SearchResponseDrug.  # noqa: E501

        For lab specific case tracking.  # noqa: E501

        :return: The case_id of this SearchResponseDrug.  # noqa: E501
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this SearchResponseDrug.

        For lab specific case tracking.  # noqa: E501

        :param case_id: The case_id of this SearchResponseDrug.  # noqa: E501
        :type: str
        """

        self._case_id = case_id

    @property
    def tiering_template(self):
        """Gets the tiering_template of this SearchResponseDrug.  # noqa: E501

        The tiering template used to assess the quality of evidence.  # noqa: E501

        :return: The tiering_template of this SearchResponseDrug.  # noqa: E501
        :rtype: str
        """
        return self._tiering_template

    @tiering_template.setter
    def tiering_template(self, tiering_template):
        """Sets the tiering_template of this SearchResponseDrug.

        The tiering template used to assess the quality of evidence.  # noqa: E501

        :param tiering_template: The tiering_template of this SearchResponseDrug.  # noqa: E501
        :type: str
        """
        if tiering_template is None:
            raise ValueError("Invalid value for `tiering_template`, must not be `None`")  # noqa: E501

        self._tiering_template = tiering_template

    @property
    def tiering_template_legend(self):
        """Gets the tiering_template_legend of this SearchResponseDrug.  # noqa: E501

        The tiering template legend explains the tiers pertaining to the template.  # noqa: E501

        :return: The tiering_template_legend of this SearchResponseDrug.  # noqa: E501
        :rtype: object
        """
        return self._tiering_template_legend

    @tiering_template_legend.setter
    def tiering_template_legend(self, tiering_template_legend):
        """Sets the tiering_template_legend of this SearchResponseDrug.

        The tiering template legend explains the tiers pertaining to the template.  # noqa: E501

        :param tiering_template_legend: The tiering_template_legend of this SearchResponseDrug.  # noqa: E501
        :type: object
        """

        self._tiering_template_legend = tiering_template_legend

    @property
    def total(self):
        """Gets the total of this SearchResponseDrug.  # noqa: E501

        The total number of records that match this search.  # noqa: E501

        :return: The total of this SearchResponseDrug.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchResponseDrug.

        The total number of records that match this search.  # noqa: E501

        :param total: The total of this SearchResponseDrug.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def total_pages(self):
        """Gets the total_pages of this SearchResponseDrug.  # noqa: E501

        The number of results pages for this search based on the limit provided in the request.  # noqa: E501

        :return: The total_pages of this SearchResponseDrug.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this SearchResponseDrug.

        The number of results pages for this search based on the limit provided in the request.  # noqa: E501

        :param total_pages: The total_pages of this SearchResponseDrug.  # noqa: E501
        :type: int
        """
        if total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def page(self):
        """Gets the page of this SearchResponseDrug.  # noqa: E501

        The results page number this response corresponds to.  # noqa: E501

        :return: The page of this SearchResponseDrug.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchResponseDrug.

        The results page number this response corresponds to.  # noqa: E501

        :param page: The page of this SearchResponseDrug.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def rows(self):
        """Gets the rows of this SearchResponseDrug.  # noqa: E501

        The array of drugs that match the search criteria.  # noqa: E501

        :return: The rows of this SearchResponseDrug.  # noqa: E501
        :rtype: list[Drug]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this SearchResponseDrug.

        The array of drugs that match the search criteria.  # noqa: E501

        :param rows: The rows of this SearchResponseDrug.  # noqa: E501
        :type: list[Drug]
        """

        self._rows = rows

    @property
    def rationalized(self):
        """Gets the rationalized of this SearchResponseDrug.  # noqa: E501

        The array of filters and how they were interpreted by the MolecularMatch search engine.  # noqa: E501

        :return: The rationalized of this SearchResponseDrug.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._rationalized

    @rationalized.setter
    def rationalized(self, rationalized):
        """Sets the rationalized of this SearchResponseDrug.

        The array of filters and how they were interpreted by the MolecularMatch search engine.  # noqa: E501

        :param rationalized: The rationalized of this SearchResponseDrug.  # noqa: E501
        :type: list[Filter]
        """

        self._rationalized = rationalized

    @property
    def unrecognized(self):
        """Gets the unrecognized of this SearchResponseDrug.  # noqa: E501

        The array of filters that were not recognized by the MolecularMatch search engine.  # noqa: E501

        :return: The unrecognized of this SearchResponseDrug.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._unrecognized

    @unrecognized.setter
    def unrecognized(self, unrecognized):
        """Sets the unrecognized of this SearchResponseDrug.

        The array of filters that were not recognized by the MolecularMatch search engine.  # noqa: E501

        :param unrecognized: The unrecognized of this SearchResponseDrug.  # noqa: E501
        :type: list[Filter]
        """

        self._unrecognized = unrecognized

    @property
    def filter_narrative(self):
        """Gets the filter_narrative of this SearchResponseDrug.  # noqa: E501

        A human readable narrative describing the search conducted. Can be used to provide \"Showing results for\" functionality.  # noqa: E501

        :return: The filter_narrative of this SearchResponseDrug.  # noqa: E501
        :rtype: str
        """
        return self._filter_narrative

    @filter_narrative.setter
    def filter_narrative(self, filter_narrative):
        """Sets the filter_narrative of this SearchResponseDrug.

        A human readable narrative describing the search conducted. Can be used to provide \"Showing results for\" functionality.  # noqa: E501

        :param filter_narrative: The filter_narrative of this SearchResponseDrug.  # noqa: E501
        :type: str
        """

        self._filter_narrative = filter_narrative

    @property
    def ambiguous_narrative(self):
        """Gets the ambiguous_narrative of this SearchResponseDrug.  # noqa: E501

        if true include a human readable ambiguous narrative.  This enables the consumer to activate \"did you mean\" search capability.  # noqa: E501

        :return: The ambiguous_narrative of this SearchResponseDrug.  # noqa: E501
        :rtype: list[str]
        """
        return self._ambiguous_narrative

    @ambiguous_narrative.setter
    def ambiguous_narrative(self, ambiguous_narrative):
        """Sets the ambiguous_narrative of this SearchResponseDrug.

        if true include a human readable ambiguous narrative.  This enables the consumer to activate \"did you mean\" search capability.  # noqa: E501

        :param ambiguous_narrative: The ambiguous_narrative of this SearchResponseDrug.  # noqa: E501
        :type: list[str]
        """

        self._ambiguous_narrative = ambiguous_narrative

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
        if issubclass(SearchResponseDrug, dict):
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
        if not isinstance(other, SearchResponseDrug):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
