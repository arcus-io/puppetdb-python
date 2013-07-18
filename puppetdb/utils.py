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
import requests
import os
import urllib
try:
    import simplejson as json
except ImportError:
    import json

def api_request(api_base_url='http://localhost:8080/', path='', method='get',
    data=None, params={}, verify=True, cert=list()):
    """
    Wrapper function for requests

    :param api_base_url: Base URL for requests
    :param path: Path to request
    :param method: HTTP method
    :param data: Data for post (ignored for GETs)
    :param params: Dict of key, value query params
    :param verify: True/False/CA_File_Name to perform SSL Verification of CA Chain
    :param cert: list of cert and key to use for client authentication

    """
    method = method.lower()
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }
    methods = {
        'get': requests.get,
        'post': requests.post,
    }
    if path[0] != '/':
        path = '/{0}'.format(path)
    if params:
        path += '?{0}'.format(urllib.urlencode(params))
    url = '{0}{1}'.format(api_base_url, path)
    resp = methods[method](url, data=json.dumps(data), headers=headers, verify=verify, cert=cert)
    return resp

def _make_api_request(api_url=None, path=None, verify=False, cert=list()):
    resp = api_request(api_url, path, verify=verify, cert=cert)
    data = json.loads(resp.content)
    return data

