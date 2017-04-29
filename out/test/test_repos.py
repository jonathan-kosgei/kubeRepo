# coding: utf-8

"""
    kubeRepo

    Manage Repos from k8s

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kube_repo
from kube_repo.rest import ApiException
from kube_repo.models.repos import Repos


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
        model = kube_repo.models.repos.Repos()


if __name__ == '__main__':
    unittest.main()