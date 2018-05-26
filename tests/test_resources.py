# -*- coding: utf-8 -*-

import time
import unittest

from pybel_artifactory import get_annotation_today, get_knowledge_today, get_namespace_today
from pybel_artifactory.constants import (
    ARTIFACTORY_ANNOTATION_BASE_URL, ARTIFACTORY_KNOWLEDGE_BASE_URL,
    ARTIFACTORY_NAMESPACE_BASE_URL,
)
from pybel_artifactory.utils import get_arty_annotation_url, get_arty_knowledge_url, get_arty_namespace_url

TEST_ANNOTATION_RESOURCE = 'neurommsig'
TEST_NAMESPACE_RESOURCE = 'hgnc'
TEST_KNOWLEDGE_RESOURCE = 'central-dogma'


class TestResources(unittest.TestCase):

    def test_get_annotation_url(self):
        url = get_arty_annotation_url(TEST_ANNOTATION_RESOURCE, '1.0.3')
        self.assertEqual('{base}/{module}/{module}-{version}.belanno'.format(
            base=ARTIFACTORY_ANNOTATION_BASE_URL,
            module=TEST_ANNOTATION_RESOURCE,
            version='1.0.3'
        ), url)

    def test_get_namespace_url(self):
        url = get_arty_namespace_url(TEST_NAMESPACE_RESOURCE, '1.0.3')
        self.assertEqual('{}/hgnc/hgnc-1.0.3.belns'.format(ARTIFACTORY_NAMESPACE_BASE_URL), url)

    def test_get_knowledge_url(self):
        url = get_arty_knowledge_url(TEST_KNOWLEDGE_RESOURCE, '1.0.3')
        self.assertEqual('{base}/{module}/{module}-{version}.bel'.format(
            base=ARTIFACTORY_KNOWLEDGE_BASE_URL,
            module=TEST_KNOWLEDGE_RESOURCE,
            version='1.0.3'
        ), url)

    def test_get_namespace_today(self):
        n = get_namespace_today(TEST_NAMESPACE_RESOURCE)
        expected = '{module}-{version}.belns'.format(
            module=TEST_NAMESPACE_RESOURCE,
            version=time.strftime('%Y%m%d'),
        )
        self.assertEqual(expected, n)

    def test_get_annotation_today(self):
        n = get_annotation_today(TEST_NAMESPACE_RESOURCE)
        expected = '{module}-{version}.belanno'.format(
            module=TEST_NAMESPACE_RESOURCE,
            version=time.strftime('%Y%m%d'),
        )
        self.assertEqual(expected, n)

    def test_get_knowledge_today(self):
        n = get_knowledge_today(TEST_KNOWLEDGE_RESOURCE)
        expected = '{module}-{version}.bel'.format(
            module=TEST_KNOWLEDGE_RESOURCE,
            version=time.strftime('%Y%m%d'),
        )
        self.assertEqual(expected, n)
