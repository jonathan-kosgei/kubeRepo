# coding: utf-8

"""
    kubeRepo

    Manage Repos from k8s

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def namespaces_namespace_repos_name_get(self, namespace, name, **kwargs):
        """
        Gets a specific Repo
        Returns a specific repo in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.namespaces_namespace_repos_name_get(namespace, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Repo's namespace (required)
        :param str name: The Repo's name (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.namespaces_namespace_repos_name_get_with_http_info(namespace, name, **kwargs)
        else:
            (data) = self.namespaces_namespace_repos_name_get_with_http_info(namespace, name, **kwargs)
            return data

    def namespaces_namespace_repos_name_get_with_http_info(self, namespace, name, **kwargs):
        """
        Gets a specific Repo
        Returns a specific repo in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.namespaces_namespace_repos_name_get_with_http_info(namespace, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Repo's namespace (required)
        :param str name: The Repo's name (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'name', 'watch']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method namespaces_namespace_repos_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `namespaces_namespace_repos_name_get`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `namespaces_namespace_repos_name_get`")


        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = {}
        if 'watch' in params:
            query_params['watch'] = params['watch']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/namespaces/{namespace}/repos/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Repo',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def repos_get(self, **kwargs):
        """
        Gets Repos
        Returns a list of repos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.repos_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Repos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.repos_get_with_http_info(**kwargs)
        else:
            (data) = self.repos_get_with_http_info(**kwargs)
            return data

    def repos_get_with_http_info(self, **kwargs):
        """
        Gets Repos
        Returns a list of repos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.repos_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Repos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/repos', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Repos',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def watch_repos_get(self, **kwargs):
        """
        Watch Repos
        Listen to events about repos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.watch_repos_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Event
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.watch_repos_get_with_http_info(**kwargs)
        else:
            (data) = self.watch_repos_get_with_http_info(**kwargs)
            return data

    def watch_repos_get_with_http_info(self, **kwargs):
        """
        Watch Repos
        Listen to events about repos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.watch_repos_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Event
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method watch_repos_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/watch/repos', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Event',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)