#!/usr/bin/env python
# Copyright (c) 2013 Arcus, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import unittest
from mock import MagicMock, patch
import requests
from puppetdb.core import PuppetDBClient
import json
import helpers

class PuppetDBClientTestCase(unittest.TestCase):
    def setUp(self):
        self._client = PuppetDBClient()

    def tearDown(self):
        pass

    @patch('puppetdb.utils.api_request')
    def test_get_nodes(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_nodes()
        self.assertEqual(len(resp), 2)
        node_0 = resp[0]
        self.assertTrue(node_0.has_key('name'))
        self.assertEqual(node_0.get('name'), 'host1')
        node_1 = resp[1]
        self.assertTrue(node_1.has_key('name'))
        self.assertEqual(node_1.get('name'), 'host2')

    @patch('puppetdb.utils.api_request')
    def test_get_node(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node('host1')
        self.assertTrue(resp.has_key('name'))
        self.assertEqual(resp.get('name'), 'host1')

    @patch('puppetdb.utils.api_request')
    def test_get_node_facts(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_facts('host1')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'architecture')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), 'amd64')

    @patch('puppetdb.utils.api_request')
    def test_get_node_fact_by_name(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_fact_by_name('host1', 'architecture')
        self.assertNotEqual(len(resp), 0)
        fact_0 = resp[0]
        self.assertTrue(fact_0.has_key('certname'))
        self.assertEqual(fact_0.get('certname'), 'host1')
        self.assertTrue(fact_0.has_key('name'))
        self.assertEqual(fact_0.get('name'), 'architecture')
        self.assertTrue(fact_0.has_key('value'))
        self.assertEqual(fact_0.get('value'), 'amd64')

    @patch('puppetdb.utils.api_request')
    def test_get_node_resources(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_resources('host1')
        self.assertNotEqual(len(resp), 0)
        res_0 = resp[0]
        self.assertTrue(res_0.has_key('certname'))
        self.assertEqual(res_0.get('certname'), 'host1')
        self.assertTrue(res_0.has_key('parameters'))
        self.assertTrue(res_0.has_key('sourceline'))
        self.assertEqual(res_0.get('sourceline'), 7)

    @patch('puppetdb.utils.api_request')
    def test_get_node_resource_by_type(self, get):
        get.side_effect = helpers.mock_api_request
        resp = self._client.get_node_resource_by_type('host1', 'Class')
        self.assertNotEqual(len(resp), 0)
