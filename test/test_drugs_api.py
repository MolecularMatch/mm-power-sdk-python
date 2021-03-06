# coding: utf-8

"""
    MolecularMatch MMPower

    MMPower API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@molecularmatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import mm_power_sdk_python
from api.drugs_api import DrugsApi  # noqa: E501
from mm_power_sdk_python.rest import ApiException


class TestDrugsApi(unittest.TestCase):
    """DrugsApi unit test stubs"""

    def setUp(self):
        self.api = api.drugs_api.DrugsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_drug(self):
        """Test case for get_drug

        Get a Drug  # noqa: E501
        """
        pass

    def test_search_drugs(self):
        """Test case for search_drugs

        Search for drugs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
