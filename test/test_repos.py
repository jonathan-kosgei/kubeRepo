# coding: utf-8

"""
    Simple API

    A simple API to learn how to write OpenAPI Specification

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.repos import Repos


class TestRepos(unittest.TestCase):
    """ Repos unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRepos(self):
        """
        Test Repos
        """
        model = swagger_client.models.repos.Repos()


if __name__ == '__main__':
    unittest.main()
