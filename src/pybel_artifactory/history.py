# -*- coding: utf-8 -*-

"""Functions for getting the history of resources."""

from .utils import get_annotation_module_url, get_knowledge_module_url, get_namespace_module_url, get_path_helper

__all__ = [
    'get_namespace_history',
    'get_annotation_history',
    'get_knowledge_history',
]


def get_namespace_history(module_name):
    """Get the Artifactory path for a namespace module.

    :param str module_name: The name of the namespace module
    :rtype: artifactory.ArtifactoryPath
    """
    return get_path_helper(module_name, get_namespace_module_url)


def get_annotation_history(module_name):
    """Get the Artifactory path for an annotation module.

    :param str module_name: The name of the annotation module
    :rtype: artifactory.ArtifactoryPath
    """
    return get_path_helper(module_name, get_annotation_module_url)


def get_knowledge_history(module_name):
    """Get the Artifactory path for a knowledge module.

    :param str module_name: The name of the knowledge module
    :rtype: artifactory.ArtifactoryPath
    """
    return get_path_helper(module_name, get_knowledge_module_url)
