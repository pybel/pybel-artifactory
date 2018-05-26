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


def get_namespace_url(module, version):
    """Get a BEL namespace file from Artifactory given the name and version.

    :param str module:
    :param str version:
    :type: str
    """
    module = module.strip('/')

    return '{module}/{name}'.format(
        module=get_namespace_module_url(module),
        name=get_namespace_file_name(module, version),
    )


def get_annotation_url(module, version):
    """Get a BEL annotation file from artifactory given the name and version.

    :param str module:
    :param str version:
    :type: str
    """
    module = module.strip('/')

    return '{module}/{name}'.format(
        module=get_annotation_module_url(module),
        name=get_annotation_file_name(module, version),
    )


def get_knowledge_url(module, version):
    """Get a BEL knowledge file from Artifactory given the name and version.

    :param str module:
    :param str version:
    :rtype: str
    """
    module = module.strip('/')

    return '{module}/{name}'.format(
        module=get_knowledge_module_url(module),
        name=get_knowledge_file_name(module, version),
    )


def _get_resource_file_name(module, version, extension):
    """

    :param str module:
    :param str version:
    :param str extension:
    :type: str
    """
    return '{module}-{version}.{extension}'.format(
        module=module.strip('/'),
        version=version,
        extension=extension,
    )


def get_namespace_file_name(module, version):
    """

    :param str module:
    :param str version:
    :type: str
    """
    return _get_resource_file_name(module, version, extension='belns')


def get_annotation_file_name(module, version):
    """

    :param str module:
    :param str version:
    :type: str
    """
    return _get_resource_file_name(module, version, extension='belanno')


def get_knowledge_file_name(module, version):
    """Format the module name and version for a BEL Script.

    :param str module:
    :param str version:
    :type: str
    """
    return _get_resource_file_name(module, version, extension='bel')


def get_namespace_module_url(module):
    """

    :param str module:
    :rtype: str
    """
    return '{base}/{module}'.format(
        base=ARTIFACTORY_NAMESPACE_BASE_URL,
        module=module.strip('/')
    )


def get_annotation_module_url(module):
    """

    :param str module:
    :rtype str
    """
    return '{base}/{module}'.format(
        base=ARTIFACTORY_ANNOTATION_BASE_URL,
        module=module.strip('/')
    )


def get_knowledge_module_url(module):
    """

    :param str module:
    :rtype str
    """
    return '{base}/{module}'.format(
        base=ARTIFACTORY_KNOWLEDGE_BASE_URL,
        module=module
    )
