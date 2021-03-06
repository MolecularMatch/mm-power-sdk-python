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


class Filter(object):
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
        'term': 'str',
        'root_term': 'str',
        'facet': 'str',
        'filter_type': 'str',
        'distance_uom': 'str',
        'postal_code': 'str',
        'country_code': 'str',
        'gene_expand': 'bool',
        'exclude_filter_only': 'bool',
        'error': 'str',
        'ambiguous': 'Filter'
    }

    attribute_map = {
        'term': 'term',
        'root_term': 'rootTerm',
        'facet': 'facet',
        'filter_type': 'filterType',
        'distance_uom': 'distanceUOM',
        'postal_code': 'postalCode',
        'country_code': 'countryCode',
        'gene_expand': 'geneExpand',
        'exclude_filter_only': 'excludeFilterOnly',
        'error': 'error',
        'ambiguous': 'ambiguous'
    }

    def __init__(self, term=None, root_term=None, facet=None, filter_type='include', distance_uom=None, postal_code=None, country_code=None, gene_expand=None, exclude_filter_only=None, error=None, ambiguous=None):  # noqa: E501
        """Filter - a model defined in Swagger"""  # noqa: E501
        self._term = None
        self._root_term = None
        self._facet = None
        self._filter_type = None
        self._distance_uom = None
        self._postal_code = None
        self._country_code = None
        self._gene_expand = None
        self._exclude_filter_only = None
        self._error = None
        self._ambiguous = None
        self.discriminator = None
        self.term = term
        if root_term is not None:
            self.root_term = root_term
        self.facet = facet
        if filter_type is not None:
            self.filter_type = filter_type
        if distance_uom is not None:
            self.distance_uom = distance_uom
        if postal_code is not None:
            self.postal_code = postal_code
        if country_code is not None:
            self.country_code = country_code
        if gene_expand is not None:
            self.gene_expand = gene_expand
        if exclude_filter_only is not None:
            self.exclude_filter_only = exclude_filter_only
        if error is not None:
            self.error = error
        if ambiguous is not None:
            self.ambiguous = ambiguous

    @property
    def term(self):
        """Gets the term of this Filter.  # noqa: E501

        The term to search.  # noqa: E501

        :return: The term of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this Filter.

        The term to search.  # noqa: E501

        :param term: The term of this Filter.  # noqa: E501
        :type: str
        """
        if term is None:
            raise ValueError("Invalid value for `term`, must not be `None`")  # noqa: E501

        self._term = term

    @property
    def root_term(self):
        """Gets the root_term of this Filter.  # noqa: E501

        The root term corresponding to the term.  Terms can be synonyms of root term, whereas the root term is what is annotated the records being searched.  # noqa: E501

        :return: The root_term of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._root_term

    @root_term.setter
    def root_term(self, root_term):
        """Sets the root_term of this Filter.

        The root term corresponding to the term.  Terms can be synonyms of root term, whereas the root term is what is annotated the records being searched.  # noqa: E501

        :param root_term: The root_term of this Filter.  # noqa: E501
        :type: str
        """

        self._root_term = root_term

    @property
    def facet(self):
        """Gets the facet of this Filter.  # noqa: E501

        The facet or domain the term belongs to.  provide PHRASE if unknown.  # noqa: E501

        :return: The facet of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this Filter.

        The facet or domain the term belongs to.  provide PHRASE if unknown.  # noqa: E501

        :param facet: The facet of this Filter.  # noqa: E501
        :type: str
        """
        if facet is None:
            raise ValueError("Invalid value for `facet`, must not be `None`")  # noqa: E501

        self._facet = facet

    @property
    def filter_type(self):
        """Gets the filter_type of this Filter.  # noqa: E501

        Inclusion or exclusion search.  # noqa: E501

        :return: The filter_type of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this Filter.

        Inclusion or exclusion search.  # noqa: E501

        :param filter_type: The filter_type of this Filter.  # noqa: E501
        :type: str
        """
        allowed_values = ["include", "exclude"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

    @property
    def distance_uom(self):
        """Gets the distance_uom of this Filter.  # noqa: E501

        Used by DISTANCE filters only.  Specify distance in kilometers or miles.  # noqa: E501

        :return: The distance_uom of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._distance_uom

    @distance_uom.setter
    def distance_uom(self, distance_uom):
        """Sets the distance_uom of this Filter.

        Used by DISTANCE filters only.  Specify distance in kilometers or miles.  # noqa: E501

        :param distance_uom: The distance_uom of this Filter.  # noqa: E501
        :type: str
        """
        allowed_values = ["mi", "km"]  # noqa: E501
        if distance_uom not in allowed_values:
            raise ValueError(
                "Invalid value for `distance_uom` ({0}), must be one of {1}"  # noqa: E501
                .format(distance_uom, allowed_values)
            )

        self._distance_uom = distance_uom

    @property
    def postal_code(self):
        """Gets the postal_code of this Filter.  # noqa: E501

        Used by DISTANCE filters only.  Specify postal code to center distance search from.  # noqa: E501

        :return: The postal_code of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Filter.

        Used by DISTANCE filters only.  Specify postal code to center distance search from.  # noqa: E501

        :param postal_code: The postal_code of this Filter.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this Filter.  # noqa: E501

        Used by DISTANCE filters only.  Specify a 2 digit ISO-3166 country code to center distance search from.  # noqa: E501

        :return: The country_code of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Filter.

        Used by DISTANCE filters only.  Specify a 2 digit ISO-3166 country code to center distance search from.  # noqa: E501

        :param country_code: The country_code of this Filter.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def gene_expand(self):
        """Gets the gene_expand of this Filter.  # noqa: E501

        Used by MUTATION filters only.  If true, expand the search to include results maching the mutation gene.  # noqa: E501

        :return: The gene_expand of this Filter.  # noqa: E501
        :rtype: bool
        """
        return self._gene_expand

    @gene_expand.setter
    def gene_expand(self, gene_expand):
        """Sets the gene_expand of this Filter.

        Used by MUTATION filters only.  If true, expand the search to include results maching the mutation gene.  # noqa: E501

        :param gene_expand: The gene_expand of this Filter.  # noqa: E501
        :type: bool
        """

        self._gene_expand = gene_expand

    @property
    def exclude_filter_only(self):
        """Gets the exclude_filter_only of this Filter.  # noqa: E501

        To create a soft include filter, add excludeFilterOnly=true (and specify filterType of include.  # noqa: E501

        :return: The exclude_filter_only of this Filter.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_filter_only

    @exclude_filter_only.setter
    def exclude_filter_only(self, exclude_filter_only):
        """Sets the exclude_filter_only of this Filter.

        To create a soft include filter, add excludeFilterOnly=true (and specify filterType of include.  # noqa: E501

        :param exclude_filter_only: The exclude_filter_only of this Filter.  # noqa: E501
        :type: bool
        """

        self._exclude_filter_only = exclude_filter_only

    @property
    def error(self):
        """Gets the error of this Filter.  # noqa: E501


        :return: The error of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Filter.


        :param error: The error of this Filter.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def ambiguous(self):
        """Gets the ambiguous of this Filter.  # noqa: E501


        :return: The ambiguous of this Filter.  # noqa: E501
        :rtype: Filter
        """
        return self._ambiguous

    @ambiguous.setter
    def ambiguous(self, ambiguous):
        """Sets the ambiguous of this Filter.


        :param ambiguous: The ambiguous of this Filter.  # noqa: E501
        :type: Filter
        """

        self._ambiguous = ambiguous

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
        if issubclass(Filter, dict):
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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
