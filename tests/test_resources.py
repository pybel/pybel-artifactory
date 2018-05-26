# -*- coding: utf-8 -*-

import time
import unittest

from pybel_artifactory import get_namespace_today
from pybel_artifactory.constants import ARTIFACTORY_ANNOTATION_BASE, ARTIFACTORY_NAMESPACE_BASE
from pybel_artifactory.utils import get_arty_annotation_url, get_arty_namespace_url

TEST_ANNOTATION_RESOURCE = 'neurommsig'
TEST_NAMESPACE_RESOURCE = 'hgnc'


class TestResources(unittest.TestCase):

    def test_get_annotation_url(self):
        url = get_arty_annotation_url(TEST_ANNOTATION_RESOURCE, '1.0.3')
        self.assertEqual('{}/neurommsig/neurommsig-1.0.3.belanno'.format(ARTIFACTORY_ANNOTATION_BASE), url)

    def test_get_namespace_url(self):
        url = get_arty_namespace_url(TEST_NAMESPACE_RESOURCE, '1.0.3')
        self.assertEqual('{}/hgnc/hgnc-1.0.3.belns'.format(ARTIFACTORY_NAMESPACE_BASE), url)

    def test_get_today(self):
        n = get_namespace_today(TEST_ANNOTATION_RESOURCE)
        expected = '{module}-{version}.belns'.format(
            module=TEST_ANNOTATION_RESOURCE,
            version=time.strftime('%Y%m%d'),
        )

        self.assertEqual(expected, n)
