# -*- coding: utf-8 -*-

"""Utilities for PyBEL Artifactory."""

from artifactory import ArtifactoryPath

from .constants import ARTIFACTORY_ANNOTATION_BASE_URL, ARTIFACTORY_KNOWLEDGE_BASE_URL, ARTIFACTORY_NAMESPACE_BASE_URL


def get_path_helper(module_name, getter):
    """Helps get the Artifactory path for a certain module

    :param str module_name: The name of the module
    :param types.FunctionType getter: The function that gets the modules from the Artifactory repository
    :rtype: artifactory.ArtifactoryPath
    """
    return ArtifactoryPath(getter(module_name))


def get_arty_namespace_module(namespace):
    """

    :param namespace:
    :return:
    """
    return '{}/{}'.format(ARTIFACTORY_NAMESPACE_BASE_URL, namespace)


def get_arty_namespace(namespace, version):
    """

    :param namespace:
    :param version:
    :return:
    """
    return '{module}-{version}.belns'.format(
        module=namespace,
        version=version
    )


def get_arty_namespace_url(namespace, version):
    """Get a BEL namespace file from artifactory given the name and version."""
    return '{module}/{name}'.format(
        module=get_arty_namespace_module(namespace),
        name=get_arty_namespace(namespace, version),
    )


def get_arty_annotation_module(module):
    """

    :param module:
    :return:
    """
    return '{base}/{module}'.format(base=ARTIFACTORY_ANNOTATION_BASE_URL, module=module)


def get_arty_annotation(module_name, version):
    """

    :param module_name:
    :param version:
    :return:
    """
    return '{module}-{version}.belanno'.format(
        module=module_name,
        version=version
    )


def get_arty_annotation_url(module, version):
    """Get a BEL annotation file from artifactory given the name and version."""
    return '{module}/{name}'.format(
        module=get_arty_annotation_module(module),
        name=get_arty_annotation(module, version),
    )


def get_arty_knowledge_module(module_name):
    """

    :param module_name:
    :return:
    """
    return '{base}/{module}'.format(base=ARTIFACTORY_KNOWLEDGE_BASE_URL, module=module_name)


def get_arty_knowledge(module, version):
    """Format the module name and version for a BEL Script.

    :param str module:
    :param str version:
    """
    return '{module}-{version}.bel'.format(module=module, version=version)


def get_arty_knowledge_url(module_name, version):
    """Get a BEL knowledge file from Artifactory given the name and version.

    :param str module_name:
    :param str version:
    :rtype: str
    """
    return '{module}/{name}'.format(
        module=get_arty_knowledge_module(module_name),
        name=get_arty_knowledge(module_name, version),
    )
