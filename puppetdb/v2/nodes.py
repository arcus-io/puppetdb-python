#!/usr/bin/env python
# Copyright (c) 2013 Arcus, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from puppetdb import utils

API_VERSION = 'v2'

def get_nodes(api_url=None, verify=False, cert=list()):
    """
    Returns info for all Nodes

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/nodes', verify=False, cert=list())

def get_node(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns info for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}'.format(node_name), verify=False, cert=list())

def get_node_facts(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns facts for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}/facts'.format(node_name), verify=False, cert=list())

def get_node_fact_by_name(api_url=None, node_name=None, fact_name=None, verify=False, cert=list()):
    """
    Returns specified fact for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node
    :param fact_name: Name of fact

    """
    return utils._make_api_request(api_url, '/nodes/{0}/facts/{1}'.format(node_name,
        fact_name), verify=False, cert=list())

def get_node_resources(api_url=None, node_name=None, verify=False, cert=list()):
    """
    Returns resources for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node

    """
    return utils._make_api_request(api_url, '/nodes/{0}/resources'.format(node_name), verify=False, cert=list())

def get_node_resource_by_type(api_url=None, node_name=None,
    type_name=None, verify=False, cert=list()):
    """
    Returns specified resource for a Node

    :param api_url: Base PuppetDB API url
    :param node_name: Name of node
    :param type_name: Type of resource

    """
    return utils._make_api_request(api_url, '/nodes/{0}/resources/{1}'.format(node_name,
        type_name), verify=False, cert=list())

def get_facts(api_url=None, query={}, verify=False, cert=list()):
    """
    Returns info for all Nodes

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/nodes', verify=False, cert=list())
