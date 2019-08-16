# coding: utf-8

"""
    MolecularMatch MMPower

    MMPower API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@molecularmatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mm_power_sdk_python.api_client import ApiClient


class DrugsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_drug(self, id, **kwargs):  # noqa: E501
        """Get a Drug  # noqa: E501

        Get a drug  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_drug(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Drug to return (required)
        :return: Drug
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_drug_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_drug_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_drug_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a Drug  # noqa: E501

        Get a drug  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_drug_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Drug to return (required)
        :return: Drug
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drug" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_drug`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/drug/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Drug',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_drugs(self, body, **kwargs):  # noqa: E501
        """Search for drugs  # noqa: E501

        Search for drugs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_drugs(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchRequest body: SearchRequest object to send to MolecularMatch for processing (required)
        :return: SearchResponseDrug
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_drugs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.search_drugs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def search_drugs_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search for drugs  # noqa: E501

        Search for drugs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_drugs_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchRequest body: SearchRequest object to send to MolecularMatch for processing (required)
        :return: SearchResponseDrug
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_drugs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `search_drugs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/drug/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResponseDrug',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
