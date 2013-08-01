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

def get_facts(api_url=None, query='', verify=False, cert=list()):
    """
    Returns facts

    :param api_url: Base PuppetDB API url

    """
    return utils._make_api_request(api_url, '/facts', verify, cert, params={'query': query})

def get_facts_by_name(api_url=None, fact_name=None, verify=False, cert=list()):
    """
    Returns facts by name

    :param api_url: Base PuppetDB API url
    :param fact_name: Name of fact

    """
    return utils._make_api_request(api_url, '/facts/{0}'.format(fact_name), verify, cert)

def get_facts_by_name_and_value(api_url=None, fact_name=None, fact_value=None, verify=False, cert=list()):
    """
    Returns facts by name and value

    :param api_url: Base PuppetDB API url
    :param fact_name: Name of fact
    :param fact_value: Value of fact

    """
    return utils._make_api_request(api_url, '/facts/{0}/{1}'.format(fact_name, fact_value), verify, cert)
