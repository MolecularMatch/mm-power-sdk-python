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
from swagger_client.models.mongo_publication_authors import MongoPublicationAuthors  # noqa: F401,E501
from swagger_client.models.object import Object  # noqa: F401,E501


class Publication(object):
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
        'mboost': 'float',
        'id': 'str',
        'pmid': 'str',
        'doi': 'str',
        'exclude': 'bool',
        'custom': 'bool',
        'source': 'str',
        'journal_name': 'str',
        'journal_iso_abbreviation': 'str',
        'title': 'str',
        'purpose': 'str',
        'background': 'str',
        'methods': 'str',
        'results': 'str',
        'conclusion': 'str',
        'conflicts': 'str',
        'fulltext': 'str',
        'citation': 'str',
        'citation_date': 'datetime',
        'link': 'str',
        'chemicals': 'list[str]',
        'keywords': 'list[str]',
        'extended_keywords': 'list[str]',
        'publication_type': 'list[str]',
        'authors': 'list[MongoPublicationAuthors]',
        'valid': 'Object',
        'valid_message': 'str'
    }

    attribute_map = {
        'mboost': 'mboost',
        'id': 'id',
        'pmid': 'pmid',
        'doi': 'doi',
        'exclude': 'exclude',
        'custom': 'custom',
        'source': 'source',
        'journal_name': 'journalName',
        'journal_iso_abbreviation': 'journalISOAbbreviation',
        'title': 'title',
        'purpose': 'purpose',
        'background': 'background',
        'methods': 'methods',
        'results': 'results',
        'conclusion': 'conclusion',
        'conflicts': 'conflicts',
        'fulltext': 'fulltext',
        'citation': 'citation',
        'citation_date': 'citation_date',
        'link': 'link',
        'chemicals': 'chemicals',
        'keywords': 'keywords',
        'extended_keywords': 'extendedKeywords',
        'publication_type': 'publicationType',
        'authors': 'authors',
        'valid': '_valid',
        'valid_message': '_validMessage'
    }

    def __init__(self, mboost=None, id=None, pmid=None, doi=None, exclude=None, custom=None, source=None, journal_name=None, journal_iso_abbreviation=None, title=None, purpose=None, background=None, methods=None, results=None, conclusion=None, conflicts=None, fulltext=None, citation=None, citation_date=None, link=None, chemicals=None, keywords=None, extended_keywords=None, publication_type=None, authors=None, valid=None, valid_message=None):  # noqa: E501
        """Publication - a model defined in Swagger"""  # noqa: E501
        self._mboost = None
        self._id = None
        self._pmid = None
        self._doi = None
        self._exclude = None
        self._custom = None
        self._source = None
        self._journal_name = None
        self._journal_iso_abbreviation = None
        self._title = None
        self._purpose = None
        self._background = None
        self._methods = None
        self._results = None
        self._conclusion = None
        self._conflicts = None
        self._fulltext = None
        self._citation = None
        self._citation_date = None
        self._link = None
        self._chemicals = None
        self._keywords = None
        self._extended_keywords = None
        self._publication_type = None
        self._authors = None
        self._valid = None
        self._valid_message = None
        self.discriminator = None
        if mboost is not None:
            self.mboost = mboost
        self.id = id
        if pmid is not None:
            self.pmid = pmid
        if doi is not None:
            self.doi = doi
        if exclude is not None:
            self.exclude = exclude
        if custom is not None:
            self.custom = custom
        self.source = source
        self.journal_name = journal_name
        if journal_iso_abbreviation is not None:
            self.journal_iso_abbreviation = journal_iso_abbreviation
        self.title = title
        if purpose is not None:
            self.purpose = purpose
        if background is not None:
            self.background = background
        if methods is not None:
            self.methods = methods
        if results is not None:
            self.results = results
        if conclusion is not None:
            self.conclusion = conclusion
        if conflicts is not None:
            self.conflicts = conflicts
        if fulltext is not None:
            self.fulltext = fulltext
        self.citation = citation
        self.citation_date = citation_date
        if link is not None:
            self.link = link
        if chemicals is not None:
            self.chemicals = chemicals
        if keywords is not None:
            self.keywords = keywords
        if extended_keywords is not None:
            self.extended_keywords = extended_keywords
        if publication_type is not None:
            self.publication_type = publication_type
        if authors is not None:
            self.authors = authors
        if valid is not None:
            self.valid = valid
        if valid_message is not None:
            self.valid_message = valid_message

    @property
    def mboost(self):
        """Gets the mboost of this Publication.  # noqa: E501


        :return: The mboost of this Publication.  # noqa: E501
        :rtype: float
        """
        return self._mboost

    @mboost.setter
    def mboost(self, mboost):
        """Sets the mboost of this Publication.


        :param mboost: The mboost of this Publication.  # noqa: E501
        :type: float
        """

        self._mboost = mboost

    @property
    def id(self):
        """Gets the id of this Publication.  # noqa: E501


        :return: The id of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Publication.


        :param id: The id of this Publication.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pmid(self):
        """Gets the pmid of this Publication.  # noqa: E501


        :return: The pmid of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._pmid

    @pmid.setter
    def pmid(self, pmid):
        """Sets the pmid of this Publication.


        :param pmid: The pmid of this Publication.  # noqa: E501
        :type: str
        """

        self._pmid = pmid

    @property
    def doi(self):
        """Gets the doi of this Publication.  # noqa: E501


        :return: The doi of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this Publication.


        :param doi: The doi of this Publication.  # noqa: E501
        :type: str
        """

        self._doi = doi

    @property
    def exclude(self):
        """Gets the exclude of this Publication.  # noqa: E501


        :return: The exclude of this Publication.  # noqa: E501
        :rtype: bool
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this Publication.


        :param exclude: The exclude of this Publication.  # noqa: E501
        :type: bool
        """

        self._exclude = exclude

    @property
    def custom(self):
        """Gets the custom of this Publication.  # noqa: E501


        :return: The custom of this Publication.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this Publication.


        :param custom: The custom of this Publication.  # noqa: E501
        :type: bool
        """

        self._custom = custom

    @property
    def source(self):
        """Gets the source of this Publication.  # noqa: E501


        :return: The source of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Publication.


        :param source: The source of this Publication.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def journal_name(self):
        """Gets the journal_name of this Publication.  # noqa: E501


        :return: The journal_name of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._journal_name

    @journal_name.setter
    def journal_name(self, journal_name):
        """Sets the journal_name of this Publication.


        :param journal_name: The journal_name of this Publication.  # noqa: E501
        :type: str
        """
        if journal_name is None:
            raise ValueError("Invalid value for `journal_name`, must not be `None`")  # noqa: E501

        self._journal_name = journal_name

    @property
    def journal_iso_abbreviation(self):
        """Gets the journal_iso_abbreviation of this Publication.  # noqa: E501


        :return: The journal_iso_abbreviation of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._journal_iso_abbreviation

    @journal_iso_abbreviation.setter
    def journal_iso_abbreviation(self, journal_iso_abbreviation):
        """Sets the journal_iso_abbreviation of this Publication.


        :param journal_iso_abbreviation: The journal_iso_abbreviation of this Publication.  # noqa: E501
        :type: str
        """

        self._journal_iso_abbreviation = journal_iso_abbreviation

    @property
    def title(self):
        """Gets the title of this Publication.  # noqa: E501


        :return: The title of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Publication.


        :param title: The title of this Publication.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def purpose(self):
        """Gets the purpose of this Publication.  # noqa: E501


        :return: The purpose of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Publication.


        :param purpose: The purpose of this Publication.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def background(self):
        """Gets the background of this Publication.  # noqa: E501


        :return: The background of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this Publication.


        :param background: The background of this Publication.  # noqa: E501
        :type: str
        """

        self._background = background

    @property
    def methods(self):
        """Gets the methods of this Publication.  # noqa: E501


        :return: The methods of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this Publication.


        :param methods: The methods of this Publication.  # noqa: E501
        :type: str
        """

        self._methods = methods

    @property
    def results(self):
        """Gets the results of this Publication.  # noqa: E501


        :return: The results of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Publication.


        :param results: The results of this Publication.  # noqa: E501
        :type: str
        """

        self._results = results

    @property
    def conclusion(self):
        """Gets the conclusion of this Publication.  # noqa: E501


        :return: The conclusion of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._conclusion

    @conclusion.setter
    def conclusion(self, conclusion):
        """Sets the conclusion of this Publication.


        :param conclusion: The conclusion of this Publication.  # noqa: E501
        :type: str
        """

        self._conclusion = conclusion

    @property
    def conflicts(self):
        """Gets the conflicts of this Publication.  # noqa: E501


        :return: The conflicts of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts):
        """Sets the conflicts of this Publication.


        :param conflicts: The conflicts of this Publication.  # noqa: E501
        :type: str
        """

        self._conflicts = conflicts

    @property
    def fulltext(self):
        """Gets the fulltext of this Publication.  # noqa: E501


        :return: The fulltext of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._fulltext

    @fulltext.setter
    def fulltext(self, fulltext):
        """Sets the fulltext of this Publication.


        :param fulltext: The fulltext of this Publication.  # noqa: E501
        :type: str
        """

        self._fulltext = fulltext

    @property
    def citation(self):
        """Gets the citation of this Publication.  # noqa: E501


        :return: The citation of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this Publication.


        :param citation: The citation of this Publication.  # noqa: E501
        :type: str
        """
        if citation is None:
            raise ValueError("Invalid value for `citation`, must not be `None`")  # noqa: E501

        self._citation = citation

    @property
    def citation_date(self):
        """Gets the citation_date of this Publication.  # noqa: E501


        :return: The citation_date of this Publication.  # noqa: E501
        :rtype: datetime
        """
        return self._citation_date

    @citation_date.setter
    def citation_date(self, citation_date):
        """Sets the citation_date of this Publication.


        :param citation_date: The citation_date of this Publication.  # noqa: E501
        :type: datetime
        """
        if citation_date is None:
            raise ValueError("Invalid value for `citation_date`, must not be `None`")  # noqa: E501

        self._citation_date = citation_date

    @property
    def link(self):
        """Gets the link of this Publication.  # noqa: E501


        :return: The link of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Publication.


        :param link: The link of this Publication.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def chemicals(self):
        """Gets the chemicals of this Publication.  # noqa: E501


        :return: The chemicals of this Publication.  # noqa: E501
        :rtype: list[str]
        """
        return self._chemicals

    @chemicals.setter
    def chemicals(self, chemicals):
        """Sets the chemicals of this Publication.


        :param chemicals: The chemicals of this Publication.  # noqa: E501
        :type: list[str]
        """

        self._chemicals = chemicals

    @property
    def keywords(self):
        """Gets the keywords of this Publication.  # noqa: E501


        :return: The keywords of this Publication.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Publication.


        :param keywords: The keywords of this Publication.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def extended_keywords(self):
        """Gets the extended_keywords of this Publication.  # noqa: E501


        :return: The extended_keywords of this Publication.  # noqa: E501
        :rtype: list[str]
        """
        return self._extended_keywords

    @extended_keywords.setter
    def extended_keywords(self, extended_keywords):
        """Sets the extended_keywords of this Publication.


        :param extended_keywords: The extended_keywords of this Publication.  # noqa: E501
        :type: list[str]
        """

        self._extended_keywords = extended_keywords

    @property
    def publication_type(self):
        """Gets the publication_type of this Publication.  # noqa: E501


        :return: The publication_type of this Publication.  # noqa: E501
        :rtype: list[str]
        """
        return self._publication_type

    @publication_type.setter
    def publication_type(self, publication_type):
        """Sets the publication_type of this Publication.


        :param publication_type: The publication_type of this Publication.  # noqa: E501
        :type: list[str]
        """

        self._publication_type = publication_type

    @property
    def authors(self):
        """Gets the authors of this Publication.  # noqa: E501


        :return: The authors of this Publication.  # noqa: E501
        :rtype: list[MongoPublicationAuthors]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this Publication.


        :param authors: The authors of this Publication.  # noqa: E501
        :type: list[MongoPublicationAuthors]
        """

        self._authors = authors

    @property
    def valid(self):
        """Gets the valid of this Publication.  # noqa: E501


        :return: The valid of this Publication.  # noqa: E501
        :rtype: Object
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Publication.


        :param valid: The valid of this Publication.  # noqa: E501
        :type: Object
        """

        self._valid = valid

    @property
    def valid_message(self):
        """Gets the valid_message of this Publication.  # noqa: E501


        :return: The valid_message of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._valid_message

    @valid_message.setter
    def valid_message(self, valid_message):
        """Sets the valid_message of this Publication.


        :param valid_message: The valid_message of this Publication.  # noqa: E501
        :type: str
        """

        self._valid_message = valid_message

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
        if issubclass(Publication, dict):
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
        if not isinstance(other, Publication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
