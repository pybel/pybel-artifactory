# -*- coding: utf-8 -*-

"""An extension for handling BEL resources with Artifactory."""

import os

__all__ = [
    'ARTIFACTORY_BASE',
    'ARTIFACTORY_NAMESPACE_BASE_URL',
    'ARTIFACTORY_ANNOTATION_BASE_URL',
    'ARTIFACTORY_KNOWLEDGE_BASE_URL',
]

_default_artifactory_base = 'https://arty.scai.fraunhofer.de/artifactory/bel'


def _get_artifactory_base():
    """Get the url of the Artifactory bucket.

    Uses the environment variable ``PYBEL_ARTIFACTORY_BASE`` or defaults to the Fraunhofer SCAI location.

    :rtype: str
    """
    return os.environ.get('PYBEL_ARTIFACTORY_BASE', _default_artifactory_base)


ARTIFACTORY_BASE = _get_artifactory_base()
ARTIFACTORY_NAMESPACE_BASE_URL = '{base}/namespace'.format(base=ARTIFACTORY_BASE)
ARTIFACTORY_ANNOTATION_BASE_URL = '{base}/annotation'.format(base=ARTIFACTORY_BASE)
ARTIFACTORY_KNOWLEDGE_BASE_URL = '{base}/knowledge'.format(base=ARTIFACTORY_BASE)
